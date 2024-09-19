import sql from './db.js'
import { uuid } from 'uuidv4'
import http from 'http'
import WebSocket, { WebSocketServer } from 'ws'


const wss = new WebSocketServer({ port: 7071 });
const sessions = new Map();
const uuid_to_conn = new Map();

wss.on('connection', ws => {
    const client_uuid = uuid();

    sessions.set(ws, 'none');

    console.log('connection');
    
    ws.on('close', () => console.log("disconnection lmao"))

    ws.on('message', async function (data) {
        
        const json = JSON.parse(data);

        if (json['type'] === 'set_event') {
            const to_set = json['event_uuid'];
            sessions.set(ws, to_set);
        } else if (json['type'] === 'want_qr') {
            if (sessions.get(ws) === 'none') {
                ws.send('event uuid is not sent so bye bye');
                ws.close();
            } else {
                const qr_current_uuid = uuid();

                const event_key = await sql`
                    select event_id
                    from qr_sessions
                    where session = ${ sessions.get(ws) }
                `

                console.log(event_key);

                if (event_key.length == 0) {
                    ws.close();
                    return;
                }

                const event_id = event_key[0].event_id;

                await sql`
                    insert into qr_sessions
                    (session, event_id)
                    values
                      (${ qr_current_uuid }, ${ event_id })
                `

                ws.send(JSON.stringify({'type': 'set_uuid', 'client_uuid': qr_current_uuid}));
                uuid_to_conn.set(qr_current_uuid, ws);
            }
        }

    });

})


http.createServer(function (req, res) {
    

}).listen(8000)

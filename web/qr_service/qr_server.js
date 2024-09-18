import sql from './db.js'
import uuid from 'uuidv4'

var http = require('http');




const WebSocket = require('ws');
const wss = new WebSocket.Server({ port: 7071 });
const sessions = new Map();
const uuid_to_conn = new Map();

wss.on('connection', ws => {
    const client_uuid = uuid();

    sessions.set(ws, 'none');
    uuid_to_conn.set(client_uuid, 

    console.log('connection');
    
    ws.on('close', () => console.log("disconnection lmao"))

    ws.on('message', data => {
        
        json = JSON.parse(data);

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
                    select 

                sql`
                    insert into qr_sessions
                    (session, event_id)
                    `

                ws.send(JSON.stringify({'type': 'set_uuid', 'client_uuid': qr_current_uuid}));
            }
        }

    });

})


http.createServer(function (req, res) {
    

}.listen(8000)


async function connectToServer() {
    //const ws = new WebSocket('wss://qr.greeneduinitiative.ru:7071');
    return new Promise((resolve, reject) => {
        const timer = setInterval(() => {
            if (ws.readyState === 1) {
                clearInterval(timer)
                resolve(ws);
            }
        }, 10);
    });
}

var qrcode;

(async function() {

    const ws = new WebSocket('ws://localhost:7070');
    while (ws.readyState !== 1) {
        await new Promise(r => setTimeout(r, 200));
    }
    //const ws = await connectToServer();
    console.log(ws);
    const urlParams = new URLSearchParams(window.location.search);

    if (urlParams.get('event_uuid') === '') {
        return;
    }

    ws.send(JSON.stringify({'type': 'set_event', 'event_uuid': urlParams.get('event_uuid')}));

    ws.onmessage = function (data) {
        console.log(data.data);
        const json = JSON.parse(data.data);

        if (qrcode) {
            qrcode.clear();
        }

        qrcode = new QRCode(document.getElementById("qrcode"), {
	    text: `http://qr.greeneduinitiative.ru/redeem/${ json['client_uuid'] }`,
        });
    };
})();

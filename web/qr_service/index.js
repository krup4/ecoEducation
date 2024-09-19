import * from "./qrcode.min.js"

async function connectToServer() {
    const ws = new WebSocket('wss://qr.greeneduinitiative.ru:7071');
    return new Promise((resolve, reject) => {
        const timer = setInterval(() => {
            if (ws.readyState === 1) {
                clearInterval(timer)
                resolve(ws);
            }
        }, 10);
    });
}

(async function() {
    const ws = await connectToServer();
    const urlParams = new URLSearchParams(window.location.search);

    if (urlParams.get('event_uuid') === '') {
        return;
    }

    ws.send(JSON.stringify({'type': 'set_event', 'event_uuid': urlParams.get('event_uuid')}));

    ws.on('message', async function (data) {
        const json = JSON.parse(data);

        var qrcode = new QRCode(document.getElementById("qrcode"), {
	    text: `http://qr.greeneduinitiative.ru/redeem/${ json['client_uuid'] }`,
	    width: 128,
	    height: 128,
	    colorDark : "#000000",
	    colorLight : "#ffffff",
	    correctLevel : QRCode.CorrectLevel.H
        });
    });
});

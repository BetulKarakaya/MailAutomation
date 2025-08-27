import asyncio
from aiosmtpd.controller import Controller

class PrintHandler:
    async def handle_DATA(self, server, session, envelope):
        print('---New Email---')
        print('From:', envelope.mail_from)
        print('To  :', envelope.rcpt_tos)
        print('Body:\n', envelope.content.decode('utf8'))
        print('----------------')
        return '250 Message accepted for delivery'

if __name__ == "__main__":
    controller = Controller(PrintHandler(), hostname='127.0.0.1', port=1025)
    controller.start()
    print("✅ Debug SMTP server running on localhost:1025")
    try:
        asyncio.get_event_loop().run_forever()
    except KeyboardInterrupt:
        controller.stop()
        print("✅ Server stopped")

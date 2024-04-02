import cv2

# Cargar la imagen
image = cv2.imread("image_mipi_9.jpg")

# Convertir la imagen a escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 

# Aplicar un umbral para segmentar la imagen
_, threshold = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

#guardarla en un archivo llamado segmentacion.jpg

cv2.imwrite("segmentacion.jpg", threshold)


# Extraer características de la imagen segmentada
# Aquí puedes agregar tu código para extraer las características deseadas

# Mostrar la imagen segmentada
cv2.imshow("Segmented Image", threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()

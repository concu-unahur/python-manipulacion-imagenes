from skimage import io, img_as_ubyte
from pathlib import Path

cwd = Path.cwd()

def armar_ruta(nombre):
  return (cwd / 'imagenes' / nombre).resolve()

def leer_imagen(nombre):
  return io.imread(armar_ruta(nombre))

def escribir_imagen(nombre, imagen):
  io.imsave(armar_ruta(nombre), img_as_ubyte(imagen))

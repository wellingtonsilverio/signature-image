# -*- coding: utf-8 -*-
# Importação de bibliotecas externas
#  Biblioteca "sys" usada para buscar os argumentos passados pelo "command line"
import sys
# 
import os
#  Biblioteca "pillow" que manipula imagens em Python Documentação em: https://pillow.readthedocs.io/en/stable/
from PIL import Image

def createSignatureImage():
    getParams()

    openImages()

    setSpaces()

    insertSignatureInImage()

    saveNewImage()

def getParams():
    global signature, figure, output, newSignatureWidth, newSignatureHeight

    signature = "logos/logo.png"
    figure = "images/image.jpg"
    output = "output/image.jpg"
    newSignatureWidth = None
    newSignatureHeight = None

    for i in range(1, len(sys.argv)):
        if (sys.argv[i][0] == '-'):
            if (sys.argv[i][1] == 's'):
                signature = sys.argv[i + 1]
            if (sys.argv[i][1] == 'p'):
                figure = sys.argv[i + 1]
            if (sys.argv[i][1] == 'o'):
                output = sys.argv[i + 1]
            if (sys.argv[i][1] == 'w'):
                newSignatureWidth = int(sys.argv[i + 1])
            if (sys.argv[i][1] == 'h'):
                newSignatureHeight = int(sys.argv[i + 1])

def openImages():
    global imgSignature, imgFigure

    imgSignature = Image.open(signature)
    imgFigure = Image.open(figure)

def getSizes():
    signatureWidth, signatureHeight = imgSignature.size
    figurWidth, figureHeight = imgFigure.size

    return signatureWidth, signatureHeight, figurWidth, figureHeight

def setSpaces():
    global spaceWidth, spaceHeight

    marginWidth = 10
    marginHeight = 10

    signatureWidth, signatureHeight, figurWidth, figureHeight = getSizes()

    if (newSignatureWidth):
        signatureWidth, signatureHeight = resizeSignareByWidth(signatureWidth, signatureHeight)
    if (newSignatureHeight):
        signatureWidth, signatureHeight = resizeSignareByWidth(signatureWidth, signatureHeight)

    spaceWidth = (figurWidth - signatureWidth) - marginWidth
    spaceHeight = (figureHeight - signatureHeight) - marginHeight

def resizeSignareByWidth(signatureWidth, signatureHeight):
    widthPorcent = newSignatureWidth / signatureWidth

    size = int(newSignatureWidth), int(signatureHeight * widthPorcent)

    imgSignature.thumbnail(size, Image.ANTIALIAS)

    return size

def resizeSignareByHeight(signatureWidth, signatureHeight):
    heightPorcent = newSignatureHeight / signatureHeight

    size = int(signatureWidth * heightPorcent), int(newSignatureHeight)

    imgSignature.thumbnail(size, Image.ANTIALIAS)

    return size

def insertSignatureInImage():
    imgFigure.paste(imgSignature, (spaceWidth, spaceHeight), imgSignature)

def saveNewImage():
    checkOutputDirectoryExists()

    imgFigure.save(output)

def checkOutputDirectoryExists():
    path = createPath(output)
    if not os.path.exists(path):
        createNewOutputDirectory(path)

def createPath(output):
    path = output.split('/')[:-1]
    newPath = ""
    for route in path:
        if route == '':
            newPath += "/"
        else:
            newPath += route + "/"
    
    return newPath

def createNewOutputDirectory(path):
    os.makedirs(path)

createSignatureImage()
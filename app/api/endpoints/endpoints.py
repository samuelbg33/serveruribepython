from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List 
from fastapi.params import Depends

from app.api.DTO.dtos import ProveedorDTO,ProveedorDTOEnvio
from app.api.models.tablas import Proveedor


rutas=APIRouter()

#Rutina para conectarnos a la BD

#Rutina para construir servicios web
def guardarProveedor(datosProveedor:ProveedorDTO):
    try:
        Proveedor(
            nombres=datosProveedor.nombres,
            documento=datosProveedor.documento,
            direccion=datosProveedor.direccion,
            ciudad=datosProveedor.ciudad,
            representante=datosProveedor.representante,
            telefonoCOntacto=datosProveedor.telefonoCOntacto,
            correo=datosProveedor.correo,
            fechaEnvio=datosProveedor.fechaEnvio,
            costoEnvio=datosProveedor.costoEnvio,
            descripcion=datosProveedor.descripcion
        ) 

    except Exception as error:
        pass
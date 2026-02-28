import json
from typing import List

class Usuario:
    def __init__(self, name: str, edad: int, sexo: str, telefono: str, email: str):
        self.name: str = edad
        self.edad: int = edad
        self.sexo: str = sexo
        self.telefono: str = telefono
        self.email: str = email
        
class Room:
    def __init__(self, id: int, tipo: str, precio: float, caracteristicas: List[str]):
        self.id: int = id
        self.tipo: str = tipo
        self.precio: float = precio
        self.caracteristicas: List[str] = caracteristicas
        
    def __str__(self):
        return f"Room ID: {self.id}, Tipo: {self.tipo}, Precio: {self.precio}, Características: {self.caracteristicas}"
    
class Motel:
    def __init__(self, usuario: Usuario, rooms: list[Room]):
        self.usuario: Usuario = usuario
        self.rooms: list[Room] = rooms
        
if __name__ == "__main__":
    with open("data.json", "r") as file:
        data = json.load(file)
        
    usuario = Usuario(
        name=data["name"],
        edad=data["edad"],
        sexo=data["sexo"],
        telefono=data["telefono"],
        email=data["email"]
    )
    
    motel = Motel(usuario=usuario)
    
    print(f"Usuario: {motel.usuario.name}, Edad: {motel.usuario.edad}, Sexo: {motel.usuario.sexo}, Telefono: {motel.usuario.telefono}, Email: {motel.usuario.email}")
    
    
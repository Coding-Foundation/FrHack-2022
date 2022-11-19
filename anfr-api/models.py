from sqlalchemy import Float, Column, ForeignKey, Date, Integer, String
from sqlalchemy.orm import relationship
from .database import Base


class SystemTelecom(Base):
    __tablename__ = "system_telecom"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    generation = Column(String, index=True)
    operator = Column(String, index=True)
    transmiters = relationship("Transmitter", back_populates="system")



class Transmitter(Base):
    __tablename__ = "transmitter"

    id = Column(Integer, primary_key=True, index=True)
    creation_date = Column(String, index=True)
    system = Column(Integer, ForeignKey("system_telecom.id"))
    antenna = Column(Integer, ForeignKey("antenna.id"))
    position = Column(Integer, ForeignKey("position.id"))
    captors = relationship("Captor", back_populates="transmitter")


class Antenna(Base):
    __tablename__ = "antenna"

    id = Column(Integer, primary_key=True, index=True)
    azimut = Column(Integer, index=True)
    altitude = Column(Integer, index=True)
    transmitter = relationship("Transmitter", back_populates="antenna")


class Position(Base):
    __tablename__ = "position"

    id = Column(Integer, primary_key=True, index=True)
    code_insee = Column(Integer, index=True)
    code_postal = Column(Integer, index=True)
    departement = Column(Integer, index=True)
    lib_dpt = Column(String, index=True)
    code_region = Column(Integer, index=True)
    lib_region = Column(String, index=True)
    lib_maj_reg = Column(String, index=True)
    altitude = Column(Integer, index=True)
    description = Column(String, index=True)
    latitude = Column(Float, index=True)
    longitude = Column(Float, index=True)


class Captor(Base):
    __tablename__ = "captor"

    id = Column(Integer, primary_key=True, index=True)
    creation_date = Column(String, index=True)
    name = Column(String, unique=True, index=True)
    address = Column(String, index=True)
    code_postal = Column(String, index=True)
    latitude = Column(Float, index=True)
    longitude = Column(Float, index=True)
    measures = relationship("Measure", back_populates="captor")
    transmitter = Column(Integer, ForeignKey("transmitter.id"))


class Measure(Base):
    __tablename__ = "measure"

    id = Column(Integer, primary_key=True, index=True)
    value = Column(Float, index=True)
    date = Column(Date, index=True)
    captor = Column(Integer, ForeignKey("captor.id"))

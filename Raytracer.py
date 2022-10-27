from gl import Raytracer, V3
from texture import *
from figures import *
from lights import *


width = 312
height = 312

# Materiales

brick = Material(diffuse = (1, 1, 1), spec = 16)
stone = Material(diffuse = (1, 1, 1), spec = 8)
grass = Material(diffuse = (0.3, 1.0, 0.3), spec = 64)


marble = Material(spec = 64, texture = Texture("marble.bmp"), matType= REFLECTIVE)

mirror = Material(diffuse = (1, 1, 1), spec = 64, matType = REFLECTIVE)
glass = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, ior = 1.5, matType = TRANSPARENT)

rtx = Raytracer(width, height)

rtx.envMap = Texture("parkingLot.bmp")

rtx.lights.append( AmbientLight(intensity = 0.25 ))
rtx.lights.append( PointLight(point = (-1,-1,0) ))
rtx.lights.append( DirectionalLight(direction=(-1, -1, -1), intensity=0.5))

rtx.scene.append( Plane(position = (0,-10,0), normal = (0,1,0), material = brick ))
rtx.scene.append( Plane(position = (0,8,0), normal = (0,-1,0), material = brick ))
rtx.scene.append( Plane(position = (-15,0,0), normal = (1,0,0), material = brick ))
rtx.scene.append( Plane(position = (15,0,0), normal = (-1,0,0), material = brick ))
rtx.scene.append( Plane(position = (0,0,-38), normal = (0,0,1), material = brick ))

rtx.scene.append( AABB(position = (-2,1,-10), size = (2,2,2), material = glass))
rtx.scene.append( AABB(position = (2,1,-10), size = (2,2,2), material = marble))

rtx.glRender()

rtx.glFinish("output.bmp")
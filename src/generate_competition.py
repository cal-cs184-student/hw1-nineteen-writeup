"""A small planet campsite made from triangles and nested SVG groups.
Run: python3 src/generate_competition.py [output.svg]
Only uses shapes supported by the homework renderer.
"""
import math, random, sys
from pathlib import Path
out=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parents[1]/'svg/extra/competition.svg'
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="800" height="800">']
def points(ps):return ' '.join(f'{x:.3f},{y:.3f}' for x,y in ps)
def poly(ps,c):parts.append(f'<polygon fill="{c}" points="{points(ps)}"/>')
def rgb(c):return [int(c[i:i+2],16)/255 for i in (1,3,5)]+[1]
def tri(ps,cs):parts.append('<colortri points="'+' '.join(f'{x:.3f} {y:.3f}' for x,y in ps)+'" colors="'+' '.join(str(v) for c in cs for v in rgb(c))+'"/>')
def disk(x,y,r,c1,c2,n=64):
    for i in range(n):
        a=i*math.tau/n;b=(i+1)*math.tau/n
        tri([(x,y),(x+r*math.cos(a),y+r*math.sin(a)),(x+r*math.cos(b),y+r*math.sin(b))],[c1,c2,c2])
tri([(0,0),(800,0),(0,800)],['#101c39','#18213e','#90658b'])
tri([(800,0),(800,800),(0,800)],['#18213e','#db8f92','#90658b'])
rng=random.Random(184)
for i in range(100):
    x=rng.uniform(20,780);y=rng.uniform(15,425);r=rng.choice([.7,1,1.5,2.2])
    poly([(x-r,y),(x,y-r),(x+r,y),(x,y+r)],rng.choice(['#dbc9b3','#a2bdce','#f4e5c7']))
# Elliptical ring segments sit behind and in front of the planet.
def ring(start,end):
    for i in range(start,end):
        a=i*math.tau/128;b=(i+1)*math.tau/128
        def pt(t,r):return (530+r*math.cos(t),205+.28*r*math.sin(t)-.26*r*math.cos(t))
        poly([pt(a,153),pt(b,153),pt(b,179),pt(a,179)],'#e7ba8d' if i%3 else '#b18587')
ring(64,128)
disk(530,205,99,'#f9cf9a','#bc717e')
ring(0,64)
disk(150,146,24,'#e8d1b6','#a5adc3',32)
# Overlapping mountains with differently colored triangle faces.
for x,y,r,c1,c2 in [(-70,520,250,'#514d73','#383e61'),(215,435,250,'#646080','#434767'),(490,470,250,'#595878','#39445f'),(760,410,300,'#6b6280','#444a69')]:
    bounded=lambda value:max(0,min(800,value))
    poly([(bounded(x-r),620),(bounded(x),y),(bounded(x+30),620)],c1)
    poly([(bounded(x),y),(bounded(x+r),620),(bounded(x+30),620)],c2)
poly([(0,574),(160,537),(350,585),(540,559),(800,600),(800,800),(0,800)],'#ba7882')
poly([(0,661),(180,618),(410,668),(680,622),(800,648),(800,800),(0,800)],'#764f70')
poly([(0,735),(310,697),(490,724),(800,670),(800,800),(0,800)],'#423953')
# A tent and its darker open door.
poly([(228,650),(323,504),(440,650)],'#f0b57c')
poly([(323,504),(440,650),(495,625),(368,512)],'#c77b6c')
poly([(248,650),(323,541),(395,650)],'#29364b')
poly([(323,541),(323,650),(395,650)],'#3c4560')
# Small robot by the tent, with a waving arm in nested local coordinates.
parts.append('<g transform="translate(565 616) rotate(-8)">')
poly([(-23,-40),(23,-40),(23,8),(-23,8)],'#3e8590')
poly([(-20,-75),(20,-75),(20,-46),(-20,-46)],'#76b0ad')
poly([(-14,-68),(14,-68),(14,-55),(-14,-55)],'#20394c')
for x in [-9,9]:poly([(x-2,-64),(x+2,-64),(x+2,-60),(x-2,-60)],'#ffd8a4')
for x in [-14,14]:poly([(x-6,8),(x+6,8),(x+9,37),(x-5,37)],'#6baba8')
parts.append('<g transform="translate(23 -32) rotate(-40)">')
poly([(0,-5),(32,-5),(32,5),(0,5)],'#76b0ad')
parts.append('<g transform="translate(32 0) rotate(-55)">')
poly([(0,-5),(24,-5),(24,5),(0,5)],'#76b0ad')
poly([(23,-8),(33,-8),(33,8),(23,8)],'#ecc091')
parts.append('</g></g></g>')
# Campfire and scattered angular rocks.
poly([(498,684),(507,654),(520,669),(530,640),(545,684)],'#dc8068')
poly([(507,684),(521,658),(532,684)],'#f7c28a')
for x,y,s in [(82,685,14),(715,748,19),(195,769,10),(655,659,8)]:
    poly([(x-s,y),(x-3,y-s/2),(x+s,y-2),(x+s/2,y+s/3)],'#aa7884')
parts.append('</svg>')
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text('\n'.join(parts))
print(out)

include <../gospel.scad>

$fn = 50;
THICK = 2;
SCREW = 6;
SCREW_HOLE = SCREW-2*THICK;
SIZE = [81, 63+27, 23];
INNER_SIZE = [SIZE.x-2*THICK, SIZE.y-2*THICK, SIZE.z];
USB_DIAMETER = 4;
USB_HEIGHT = 10;
KEY_HOLE = [14, 14, 14];
KEY_SPACING = KEY_HOLE.x + 5;
ENCODER_HOLE = 7;
KNOB_DIAMETER = 25;
KNOB_INNER_DIAMETER = 20;
KNOB_NOTCH = 6;
KNOB_HOLE = 6.5;
KNOB_GROOVE_WIDTH = 5;
KNOB_GROOVE_DEPTH = 9;
KNOB_HOLE_DEPTH = 13;
KNOB_DEPTH = KNOB_HOLE_DEPTH+THICK;

z(SIZE.z)
lid();
bin();
knobs();


module bin() {
    difference() {
        cube(SIZE, center=true);
        
        z(THICK) cube(INNER_SIZE, center=true);
        
        x(SIZE.x/2-THICK/2) z(2*THICK)
        cube([2*THICK, USB_DIAMETER, SIZE.z], center=true);
    }
    
    dx() dy()
    x(SIZE.x/2-SCREW/2)
    y(SIZE.y/2-SCREW/2)
    z(-SIZE.z/2)
    pin();
}

module pin() {
    difference() {
        cylinder(h=SIZE.z, d=SCREW);
        cylinder(h=2*SIZE.z, d=SCREW_HOLE);
    }
}

module lid() {
    difference() {
        cube([SIZE.x, SIZE.y, THICK], center=true);
            
        dx() dy()
        x(SIZE.x/2-SCREW/2)
        y(SIZE.y/2-SCREW/2)
        cylinder(h=2*SIZE.z, d=SCREW_HOLE, center=true);
        
        y(THICK-SIZE.y/2)
        for (i = [0:2]) {
            y(i*KEY_SPACING)
            dx()
            for (j = [0:1]) {
                x(KEY_SPACING/2 + j*KEY_SPACING)
                y(KEY_SPACING/2)
                cube(KEY_HOLE, center=true);
            }
        }
        
        for(e = [0:2]) {
            x((e-1)*SIZE.x/3)
            y(SIZE.y/2-KEY_SPACING+2*THICK)
            cylinder(h=2*SIZE.z, d=ENCODER_HOLE, center=true);
        }
    }
}

module knobs() {
    color("blue")
    z(SIZE.z+KNOB_DEPTH/2)
    for(k = [0:2]) {
        x((k-1)*SIZE.x/3)
        y(SIZE.y/2-KEY_SPACING+2*THICK)
        knob();
    }
}

module knob() {
    intersection() {
        difference() {
            cylinder(h=KNOB_DEPTH, d=KNOB_DIAMETER, center=true);
            
            z(-THICK)
            cylinder(h=KNOB_DEPTH, d=KNOB_INNER_DIAMETER, center=true);
            
            // Notches
            for (theta = [0:30:330]) {
                rz(theta)
                x(KNOB_DIAMETER/2+0.75*THICK)
                cylinder(h=KNOB_DEPTH+0.1, d=KNOB_NOTCH, center=true);
            }
        }
        // Bevel
        cylinder(h=2*KNOB_DEPTH, d1=3*KNOB_DIAMETER, d2=0, center=true);
    }    
    
    // Hole
    z(KNOB_HOLE_DEPTH/2-KNOB_DEPTH/2)
    difference() {
        cylinder(h=KNOB_HOLE_DEPTH, d=KNOB_HOLE+2*THICK, center=true);
        
        difference() {
            cylinder(h=KNOB_HOLE_DEPTH+0.1, d=KNOB_HOLE, center=true);
            
            x(KNOB_GROOVE_WIDTH)
            z(KNOB_DEPTH-KNOB_GROOVE_DEPTH)
            cube([KNOB_HOLE, KNOB_HOLE, KNOB_DEPTH], center=true);
        }
        
    }
}
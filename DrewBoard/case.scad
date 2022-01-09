include <../../gospel/gospel.scad>

$fn = 50;
THICK = 2;

ENCODER_HOLE = 7;

// Knob
KNOB_DIAMETER = 25;
KNOB_SPACING = KNOB_DIAMETER + 5;
KNOB_INNER_DIAMETER = 20;
KNOB_NOTCH = 6;
KNOB_HOLE = 6.5;
KNOB_GROOVE_WIDTH = 5;
KNOB_GROOVE_DEPTH = 9;
KNOB_HOLE_DEPTH = 13;
KNOB_DEPTH = KNOB_HOLE_DEPTH + THICK;

ENCODER_BOARD_LENGTH = 32;
BOX_WIDTH = ENCODER_BOARD_LENGTH + 2 * THICK;
BOX_LENGTH = 8 * KNOB_SPACING;
BOX_HEIGHT = 20 + 2 * THICK;

case([9, 1]);
z(-10)
bottom([9, 1]);

module case(numKnobs) {
    color("blue")
    difference() {
        z(-BOX_HEIGHT/2) union() {
            x(BOX_LENGTH / 2) cube([BOX_LENGTH, BOX_WIDTH, BOX_HEIGHT], center=true);
            cylinder(h=BOX_HEIGHT, d=BOX_WIDTH, center=true);
            x(BOX_LENGTH) cylinder(h=BOX_HEIGHT, d=BOX_WIDTH, center=true);
        }
        
        z(-BOX_HEIGHT/2 - THICK) {
            x(BOX_LENGTH / 2) cube([BOX_LENGTH - 2 * THICK, BOX_WIDTH - 2 * THICK, BOX_HEIGHT], center=true);
            cylinder(h=BOX_HEIGHT, d=BOX_WIDTH - 2 * THICK, center=true);
            x(BOX_LENGTH) cylinder(h=BOX_HEIGHT, d=BOX_WIDTH - 2 * THICK, center=true);
        }
        
        for(i = [0:numKnobs.x-1]) {
            for(j = [0:numKnobs.y-1]) {
                x(i*KNOB_SPACING)
                y(j*KNOB_SPACING)
                cylinder(h=BOX_HEIGHT, d=ENCODER_HOLE, center=true);
            }
        }
    }
    
    z(10)
    color("purple") {
        for(i = [0:numKnobs.x-1]) {
            for(j = [0:numKnobs.y-1]) {
                x(i*KNOB_SPACING)
                y(j*KNOB_SPACING)
                knob();
            }
        }
    }
}

module bottom(numKnobs) {
    color("green") {
        z(-BOX_HEIGHT) union() {
            x(BOX_LENGTH / 2) cube([BOX_LENGTH, BOX_WIDTH, THICH], center=true);
            cylinder(h=THICH, d=BOX_WIDTH, center=true);
            x(BOX_LENGTH) cylinder(h=THICH, d=BOX_WIDTH, center=true);
        }
        
    }
    
    z(10)
    color("purple") {
        for(i = [0:numKnobs.x-1]) {
            for(j = [0:numKnobs.y-1]) {
                x(i*KNOB_SPACING)
                y(j*KNOB_SPACING)
                knob();
            }
        }
    }
}


module knob() {
    z(KNOB_DEPTH/2) {
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
}

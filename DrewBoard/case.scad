include <../../gospel/gospel.scad>

$fn = 50;
THICK = 5;

ENCODER_HOLE = 7;

// Knob
KNOB_THICK = 2;
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
BOX_HOLE_OFFSET = 15;
BOX_WIDTH = 46; // ENCODER_BOARD_LENGTH + 2 * THICK;
BOX_LENGTH = 8 * KNOB_SPACING;
BOX_HEIGHT = 30 + 2 * THICK;

case([9, 1]);
z(-10)
bottom([9, 1]);

    
z(10)
color("#222222") {
    y(BOX_WIDTH/2 - BOX_HOLE_OFFSET)
    for(i = [0:8]) {
        x(i*KNOB_SPACING)
        knob();
    }
}
    
module case(numKnobs) {
    color("silver")
    difference() {
        z(-BOX_HEIGHT/2) union() {
            x(BOX_LENGTH / 2) cube([BOX_LENGTH, BOX_WIDTH, BOX_HEIGHT], center=true);
            cylinder(h=BOX_HEIGHT, d=BOX_WIDTH, center=true);
            x(BOX_LENGTH) cylinder(h=BOX_HEIGHT, d=BOX_WIDTH, center=true);
        }
        
        z(-BOX_HEIGHT/2 - THICK/2) {
            x(BOX_LENGTH / 2) cube([BOX_LENGTH - 1 * THICK, BOX_WIDTH - 1 * THICK, BOX_HEIGHT], center=true);
            cylinder(h=BOX_HEIGHT, d=BOX_WIDTH - 1 * THICK, center=true);
            x(BOX_LENGTH) cylinder(h=BOX_HEIGHT, d=BOX_WIDTH - 1 * THICK, center=true);
            
            // USB
            z(22.5 - BOX_HEIGHT + THICK) 
            x(-BOX_WIDTH/2) 
            cube([10,5,10], center=true);
        }
        
        // Holes
        y(BOX_WIDTH/2 - BOX_HOLE_OFFSET)
        for(i = [0:numKnobs.x-1]) {
            for(j = [0:numKnobs.y-1]) {
                x(i*KNOB_SPACING)
                y(j*KNOB_SPACING)
                cylinder(h=BOX_HEIGHT, d=ENCODER_HOLE, center=true);
            }
        }
    }
}

module bottom(numKnobs) {
    color("#222222") {
        z(-BOX_HEIGHT) union() {
            x(BOX_LENGTH / 2) cube([BOX_LENGTH, BOX_WIDTH, THICK/2], center=true);
            cylinder(h=THICK/2, d=BOX_WIDTH, center=true);
            x(BOX_LENGTH) cylinder(h=THICK/2, d=BOX_WIDTH, center=true);
        }
        
        z(THICK/2-BOX_HEIGHT) union() {
            x(BOX_LENGTH / 2) cube([BOX_LENGTH-2*THICK-1, BOX_WIDTH-1*THICK-1, THICK/2], center=true);
            cylinder(h=THICK/2, d=BOX_WIDTH-THICK-1, center=true);
            x(BOX_LENGTH) cylinder(h=THICK/2, d=BOX_WIDTH-THICK-1, center=true);
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
                    x(KNOB_DIAMETER/2+0.75*KNOB_THICK)
                    cylinder(h=KNOB_DEPTH+0.1, d=KNOB_NOTCH, center=true);
                }
            }
            // Bevel
            cylinder(h=2*KNOB_DEPTH, d1=3*KNOB_DIAMETER, d2=0, center=true);
        }    
        
        // Hole
        z(KNOB_HOLE_DEPTH/2-KNOB_DEPTH/2)
        difference() {
            cylinder(h=KNOB_HOLE_DEPTH, d=KNOB_HOLE+2*KNOB_THICK, center=true);
            
            difference() {
                cylinder(h=KNOB_HOLE_DEPTH+0.1, d=KNOB_HOLE, center=true);
                
                x(KNOB_GROOVE_WIDTH)
                z(KNOB_DEPTH-KNOB_GROOVE_DEPTH)
                cube([KNOB_HOLE, KNOB_HOLE, KNOB_DEPTH], center=true);
            }
        }
    }
}

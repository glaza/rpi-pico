use <Bonhomme.scad>;

ROUNDING = 2;
THICK = 2;
USB_DIAMETER = 4;
USB_HEIGHT = 10;
STEM_DEPTH = 5;
STEM_WIDTH = 4.5;
STEM_HEIGHT = 4.5;
STEM_THICKNESS = 1.5;
KEY_HOLE = [14, 14, 25];
KEY_DEPTH = STEM_DEPTH + THICK/2 - ROUNDING;
KEY_SPACING = 19;
ENCODER_HOLE = 7;
TOP_CASE_DEPTH = 10;
BOTTOM_CASE_DEPTH = 5;
KNOB_HOLE = 6.5;
KNOB_GROOVE_WIDTH = 5;
KNOB_GROOVE_DEPTH = 9;
KNOB_HOLE_DEPTH = 13;
KNOB_DEPTH = KNOB_HOLE_DEPTH + THICK - ROUNDING;
SCREW_SHAFT_DIAMETER = 3;
SCREW_HOLE_DIAMETER = 4;
SCREW_HEAD_DIAMETER = 10;
SCREW_POS = [
    [21, -50, -0.01],
    [-18, -46, -0.01],
    [32, 40, -0.01],
    [-20, 51, -0.01]
];

$fn = 20;

//color("pink")
//cube([20, 50, 10], center = true);

color("white")
!top_case(TOP_CASE_DEPTH);

translate([100, 0, 0])
bottom_case(BOTTOM_CASE_DEPTH);

translate([0, 0, TOP_CASE_DEPTH + 1])
color("red", 0.5) {
    left_top_cap(KEY_DEPTH);
    left_middle_cap(KEY_DEPTH);
    left_bottom_cap(KEY_DEPTH);
    right_top_cap(KEY_DEPTH);
    right_middle_cap(KEY_DEPTH);
    right_bottom_cap(KEY_DEPTH);
    knob(KNOB_DEPTH);
}

module knob(knobDepth) {
    scale([2.25, 2.25, 1]) {
        union() {
            difference() {
                minkowski() {  
                    translate([55.5, 2.5, 0])
                    scale([0.75, 0.75, 1])
                    bonhomme_head(knobDepth);
                    
                    half_sphere();
                }
                
                scale([0.9, 0.9, 0.86])
                minkowski() {  
                    translate([55.5, 4.25, -0.01])
                    scale([0.75, 0.75, 1])
                    bonhomme_head(knobDepth);
                    
                    half_sphere();
                }
            }
            
            // Stem
            scale([1/2.25, 1/2.25, 1])
            translate([1.25, 35.5, KNOB_HOLE_DEPTH/2]) {
                difference() {
                    cylinder(h=KNOB_HOLE_DEPTH, d1=KNOB_HOLE+3*THICK, d2=KNOB_HOLE+4*THICK, center=true);
                    
                    difference() {
                        cylinder(h=KNOB_HOLE_DEPTH+0.1, d=KNOB_HOLE, center=true);
                        
                        translate([KNOB_GROOVE_WIDTH, 0, KNOB_DEPTH-KNOB_GROOVE_DEPTH])
                        cube([KNOB_HOLE, KNOB_HOLE, KNOB_DEPTH], center=true);
                    }
                }
            }
        }
    }
}

module left_top_cap(keyDepth) {
    scale([2.25, 2.25, 1]) {
        union() {
            difference() {
                bonhomme_left_leg_rounded(keyDepth);
                
                difference() {
                    translate([-1.2, 0, -0.01])
                    scale([0.85, 0.85, 0.8])
                    bonhomme_left_leg_rounded(keyDepth);
                
                    translate([0, -24.2, 0])
                    rotate([0, 0, 9])
                    cube([50,50,50], center=true);
                }            
                    
                translate([0, -25, 0])
                rotate([0, 0, 9])
                cube([50,50,50], center=true);
            }

            translate([-12, -0.7, 0])
            rotate([0, 0, 9])
            scale([1/2.25, 1/2.25, 1])
            key_stem();
        }
    }
}

module left_middle_cap(keyDepth) {
    scale([2.25, 2.25, 1]) {
        union() {
            difference() {
                bonhomme_left_leg_rounded(keyDepth);
                
                difference() {
                    translate([-1.2, 0, -0.01])
                    scale([0.85, 0.85, 0.8])
                    bonhomme_left_leg_rounded(keyDepth);
                
                    translate([0, 24.5, 0])
                    rotate([0, 0, 9])
                    cube([50,50,50], center=true);
                    
                    translate([0, -33, 0])
                    rotate([0, 0, 9])
                    cube([50,50,50], center=true);
                }
                
                translate([0, 25, 0])
                rotate([0, 0, 9])
                cube([50,50,50], center=true);
                
                translate([0, -33.5, 0])
                rotate([0, 0, 9])
                cube([50,50,50], center=true);
            }
        

            translate([-3.15, -7.9, 0])
            rotate([0, 0, 99])
            scale([1/2.25, 1/2.25, 1])
            key_stem();
        }
    }
}

module left_bottom_cap(keyDepth) {
    scale([2.25, 2.25, 1]) {
        union() {
            difference() {
                bonhomme_left_leg_rounded(keyDepth);
               
                difference() {
                    translate([-1, -2, -0.01])
                    scale([0.85, 0.85, 0.8])
                    bonhomme_left_leg_rounded(keyDepth);
                
                    translate([0, 16, 0])
                    rotate([0, 0, 9])
                    cube([50,50,50], center=true);
                }
                
                translate([0, 16.5, 0])
                rotate([0, 0, 9])
                cube([50,50,50], center=true);
            }
            
            translate([-9.4, -17.4, 0])
            rotate([0, 0, 9])
            scale([1/2.25, 1/2.25, 1])
            key_stem();
        }
    }
}



module right_top_cap(keyDepth) {
    scale([2.25, 2.25, 1]) {
        union() {
            difference() {
                bonhomme_right_leg_rounded(keyDepth);
                
                difference() {
                    translate([1.25, 0, -0.01])
                    scale([0.85, 0.85, 0.8])
                    bonhomme_right_leg_rounded(keyDepth);
                
                    translate([0, -24, 0])
                    rotate([0, 0, -9])
                    cube([50,50,50], center=true);
                }  
                
                translate([0, -24.8, 0])
                rotate([0, 0, -9])
                cube([50,50,50], center=true);
            }
            
            translate([7.15, 0, 0])
            rotate([0, 0, -9])
            scale([1/2.25, 1/2.25, 1])
            key_stem();
        }
    }
}

module right_middle_cap(keyDepth) {
    scale([2.25, 2.25, 1]) {    
        union() {
            difference() {
                bonhomme_right_leg_rounded(keyDepth);
            
                difference() {
                    translate([1.25, 0, -0.01])
                    scale([0.85, 0.85, 0.8])
                    bonhomme_right_leg_rounded(keyDepth);
                
                    translate([0, 24.5, 0])
                    rotate([0, 0, -9])
                    cube([50,50,50], center=true);
                    
                    translate([0, -32.75, 0])
                    rotate([0, 0, -9])
                    cube([50,50,50], center=true);
                }
                
                translate([0, 25.2, 0])
                rotate([0, 0, -9])
                cube([50,50,50], center=true);
                
                translate([0, -33.5, 0])
                rotate([0, 0, -9])
                cube([50,50,50], center=true);
            }
            
            translate([5, -1.9, 0])
            rotate([0, 0, -99])
            scale([1/2.25, 1/2.25, 1])
            key_stem();
        }
    }
}

module right_bottom_cap(keyDepth) {
    scale([2.25, 2.25, 1]) {  
        union() {
            difference() {
                bonhomme_right_leg_rounded(keyDepth);
               
                difference() {
                    translate([1.25, -2, -0.01])
                    scale([0.85, 0.85, 0.8])
                    bonhomme_right_leg_rounded(keyDepth);
                
                    translate([0, 16, 0])
                    rotate([0, 0, -10])
                    cube([50,50,50], center=true);
                }
                
                translate([0, 16.75, 0])
                rotate([0, 0, -10])
                cube([50,50,50], center=true);
            }
            
            translate([4.6, -16.65, 0])
            rotate([0, 0, -9])
            scale([1/2.25, 1/2.25, 1])
            key_stem();
        }
    }
}


module bonhomme_left_leg_rounded(keyDepth) {
    minkowski() {
        translate([53, 0, 0])
        scale([0.75, 0.75, 1])
        bonhomme_left_leg(KEY_DEPTH);
    
        half_sphere();
    }
}

module bonhomme_right_leg_rounded(keyDepth) {
    minkowski() {
        translate([57, 0, 0])
        scale([0.75, 0.75, 1])
        bonhomme_right_leg(KEY_DEPTH);
              
        half_sphere();
    }
}
    
module top_case(case_depth) {
    
    for (screw_pos = SCREW_POS) {
        translate(screw_pos) screw_shaft(case_depth);
    }
    
    difference() {
        scale([2.25, 2.25, 1])
        minkowski() {
            linear_extrude(case_depth - ROUNDING)
            scale([0.23, 0.21, 1])
            translate([-85 , -128, 0])
            import("InteleCase.dxf");
            
            half_sphere();
        }
        
        translate([0, 0, -0.01])
        scale([2.15, 2.15, 0.85])
        minkowski() {
            linear_extrude(case_depth - ROUNDING)
            scale([0.23, 0.21, 1])
            translate([-85 , -128, 0])
            import("InteleCase.dxf");
            
            half_sphere();
        }
        
        // Encoder Hole
        translate([1, 35, -0.01])
        cylinder(h=25, d=ENCODER_HOLE);
        
        // Right
        translate([16, 0, 0])
        rotate([0, 0, -9]) {
            translate([0, 0, 0])
            key_hole();
            
            translate([-4, -KEY_SPACING, 0])
            key_hole();
            
            translate([0, -2*KEY_SPACING, 0])
            key_hole();
        }
        
        // Left      
        translate([-28, -2, 0])  
        rotate([0, 0, 9]) {
            translate([1, 0, 0])  
            key_hole();
            
            translate([4, -KEY_SPACING, 0])  
            key_hole();
            
            translate([1, -2*KEY_SPACING, 0])  
            key_hole();
        }
        
        // USB
        translate([0, 65, 0])
        rotate([90, 0, 0])
        cylinder(h=20, d=USB_DIAMETER);
    }
}

module bottom_case(case_depth) {
    
    scale([1, 1, -1]) {
        for (screw_pos = SCREW_POS) {
            translate(screw_pos) screw_hole(case_depth);
        }
        
        difference() {
            scale([2.25, 2.25, 1])
            minkowski() {
                linear_extrude(case_depth - ROUNDING)
                scale([0.23, 0.21, 1])
                translate([-85 , -128, 0])
                import("InteleCase.dxf");
                
                half_sphere();
            }
            
            translate([0, 0, -0.01])
            scale([2.15, 2.15, 0.85])
            minkowski() {
                linear_extrude(case_depth - ROUNDING)
                scale([0.23, 0.21, 1])
                translate([-85 , -128, 0])
                import("InteleCase.dxf");
                
                half_sphere();
            }
            
            for (screw_pos = SCREW_POS) {
                translate(screw_pos) screw_cutout(case_depth);
            }
            
            // USB
            translate([0, 65, 0])
            rotate([90, 0, 0])
            cylinder(h=20, d=USB_DIAMETER);
        }
    }
}

module key_hole() {
    translate([0, 0, -0.01])
    cube(KEY_HOLE);
}

module key_stem() {
    translate([7, 7, STEM_DEPTH/2]) {
        difference() {
            cube([4.5, 6.5, STEM_DEPTH], center=true);
            cube([STEM_WIDTH, STEM_THICKNESS, 2*STEM_DEPTH], center=true);
            cube([STEM_THICKNESS, STEM_HEIGHT, 2*STEM_DEPTH], center=true);
        }
    }    
}
module half_sphere() {
    difference() {
        sphere(ROUNDING, $fn = 20);
        
        translate([0, 0, -5])
        cube([10, 10, 10], center=true);
    }
}
module screw_shaft(case_depth) {
    difference() {
        cylinder(h=case_depth - THICK/2, d=SCREW_SHAFT_DIAMETER + 2*THICK);
        translate([0, 0, -0.01])
        cylinder(h=2*case_depth, d=SCREW_SHAFT_DIAMETER);
    }
}

module screw_hole(case_depth) {
    difference() {
        cylinder(h=case_depth - THICK/2, d=SCREW_HEAD_DIAMETER + 2*THICK);
        translate([0, 0, -0.01])
        cylinder(h=2*case_depth, d=SCREW_HEAD_DIAMETER);
    }
    difference() {
        cylinder(h=THICK, d=SCREW_HEAD_DIAMETER + 2*THICK);
        translate([0, 0, -0.01])
        cylinder(h=2*case_depth, d=SCREW_HOLE_DIAMETER);
    }
}
module screw_cutout(case_depth) {
        cylinder(h=2*case_depth, d=SCREW_HEAD_DIAMETER);
}
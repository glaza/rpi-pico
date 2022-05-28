use <Bonhomme.scad>;

USB_DIAMETER = 4;
USB_HEIGHT = 10;
KEY_HOLE = [14, 14, 25];
KEY_DEPTH = 5;
ENCODER_HOLE = 7;
CASE_DEPTH = 10;
ROUNDING = 2;
$fn = 20;

color("white")
case();

translate([0, 0, CASE_DEPTH + 1])
color("red", 0.3) {
    scale([2, 2, 1])
    minkowski() {
        union() {
            translate([53, 0, 0])
            scale([0.75, 0.75, 1])
            bonhomme_left_leg(KEY_DEPTH);
            
            translate([57, 0, 0])
            scale([0.75, 0.75, 1])
            bonhomme_right_leg(KEY_DEPTH);
                
            translate([55.5, 2.5, 0])
            scale([0.75, 0.75, 1])
            bonhomme_head(KEY_DEPTH);
        }
        half_sphere();
    }
}

module case() {
    difference() {
        scale([2, 2, 1])
        minkowski() {
            linear_extrude(CASE_DEPTH - ROUNDING)
            scale([0.23, 0.21, 1])
            translate([-85 , -128, 0])
            import("InteleCase.dxf");
            
            half_sphere();
        }
        
        // Encoder Hole
        translate([1, 31.5, -0.01])
        cylinder(h=25, d=ENCODER_HOLE);
        
        translate([15, 7, 0])
        rotate([0, 0, -10])
        key_hole();
        
        translate([10, -9, 0])
        rotate([0, 0, -10])
        key_hole();
        
        translate([7, -25, 0])
        rotate([0, 0, -10])
        key_hole();
        
        translate([8, -42, 0])
        rotate([0, 0, -10])
        key_hole();
        
        translate([-25, -2, 0])
        rotate([0, 0, 10])
        key_hole();
        
        translate([-20, -19, 0])
        rotate([0, 0, 10])
        key_hole();
        
        translate([-20, -36, 0])
        rotate([0, 0, 10])
        key_hole();
    }
}

module key_hole() {
    translate([0, 0, -0.01])
    cube(KEY_HOLE);
}

module half_sphere() {
    difference() {
        sphere(ROUNDING, $fn = 20);
        
        translate([0, 0, -5])
        cube([10, 10, 10], center=true);
    }
}
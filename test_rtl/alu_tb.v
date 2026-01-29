`timescale 1ns/1ps

module alu_tb;

reg  [3:0] a;
reg  [3:0] b;
reg  [1:0] op;
wire [3:0] y;

alu dut(.a(a), .b(b), .op(op), .y(y));

initial begin
    $dumpfile("dump.vcd");
    $dumpvars(0, alu_tb);

    a = 4'd3; b = 4'd2; op = 2'b00; #10;  // add
    a = 4'd7; b = 4'd1; op = 2'b01; #10;  // sub
    a = 4'd5; b = 4'd3; op = 2'b10; #10;  // and
    a = 4'd9; b = 4'd6; op = 2'b11; #10;  // or

    $finish;
end

endmodule
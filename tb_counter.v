`timescale 1ns/1ps

module tb_counter;
    // Signals
    reg clk;
    reg rst;
    wire [3:0] count;

    // Instantiate Design Under Test (DUT)
    counter_4bit dut (
        .clk(clk),
        .rst(rst),
        .count(count)
    );

    // Clock Generation (10ns period -> 100MHz)
    initial begin
        clk = 0;
        forever #5 clk = ~clk;
    end

    // Test Sequence
    initial begin
        $dumpfile("dump.vcd");
        $dumpvars(0, tb_counter);

        // Initialize Inputs
        rst = 1;

        // Wait for a few clocks
        #20;
        
        // Release Reset (Synchronous)
        @(posedge clk);
        rst = 0;
        $display("[%0t] Reset released", $time);

        // Wait for counter to count up to 15 (overflow)
        wait (count == 4'd15);
        @(posedge clk); // Capture the 15
        @(posedge clk); // Rollover to 0
        
        if (count == 4'd0) begin
             $display("[%0t] SUCCESS: Counter rolled over to 0", $time);
        end else begin
             $display("[%0t] ERROR: Counter did not roll over correctly. Count: %d", $time, count);
        end

        #20;
        $finish;
    end

    // Monitor
    initial begin
        $monitor("Time=%0t | rst=%b | count=%d", $time, rst, count);
    end

endmodule

EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 3
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Sheet
S 3800 2650 1300 1225
U 5F80A4DE
F0 "ACE1" 50
F1 "DA26R_ACE1.sch" 50
F2 "INT_B" I R 5100 3000 50 
F3 "INT_A" I R 5100 2850 50 
F4 "HEART" I R 5100 3225 50 
$EndSheet
$Sheet
S 6800 2650 1300 1225
U 5F80A61F
F0 "ACE2" 50
F1 "DA26R_ACE2.sch" 50
F2 "INT_B" I L 6800 3000 50 
F3 "INT_A" I L 6800 2850 50 
F4 "HEART" I L 6800 3225 50 
$EndSheet
Text Notes 9400 7125 0    50   ~ 0
Ruslan Pidoprygora
Wire Wire Line
	5100 2850 5375 2850
Wire Wire Line
	5100 3000 5450 3000
$Comp
L VolzLib:R0603 R61
U 1 1 60ED569D
P 5925 3225
F 0 "R61" V 5825 3250 50  0000 C CNN
F 1 "1k" V 6025 3250 50  0000 C CNN
F 2 "VolzLib:R0603" V 5855 3225 50  0001 C CNN
F 3 "~" H 5925 3225 50  0001 C CNN
	1    5925 3225
	0    1    1    0   
$EndComp
Wire Wire Line
	5100 3225 5825 3225
Wire Wire Line
	6075 3225 6800 3225
$Comp
L VolzLib:Conn_Molex_Picoblade_01x04 J13
U 1 1 6114AB37
P 6025 2475
F 0 "J13" H 5950 2675 50  0000 L CNN
F 1 "RS485" H 5925 2175 50  0000 L CNN
F 2 "VolzLib:Molex_PicoBlade_53047-0410_1x04_P1.25mm_Vertical" H 6025 2475 50  0001 C CNN
F 3 "https://www.mouser.de/datasheet/2/276/0530470310_PCB_HEADERS-170987.pdf" H 6025 2475 50  0001 C CNN
F 4 "538-53047-0410" H 6025 2475 50  0001 C CNN "Mouser-Nr."
	1    6025 2475
	1    0    0    -1  
$EndComp
Wire Wire Line
	5825 2375 5375 2375
Wire Wire Line
	5375 2375 5375 2850
Connection ~ 5375 2850
Wire Wire Line
	5375 2850 6800 2850
Wire Wire Line
	5825 2475 5450 2475
Wire Wire Line
	5450 2475 5450 3000
Connection ~ 5450 3000
Wire Wire Line
	5450 3000 6800 3000
$Comp
L VolzLib:GND #PWR0174
U 1 1 6114C231
P 5700 2650
F 0 "#PWR0174" H 5700 2400 50  0001 C CNN
F 1 "GND" H 5700 2500 50  0001 C CNN
F 2 "" H 5700 2650 50  0001 C CNN
F 3 "" H 5700 2650 50  0001 C CNN
	1    5700 2650
	1    0    0    -1  
$EndComp
Wire Wire Line
	5700 2650 5700 2575
Wire Wire Line
	5700 2575 5825 2575
NoConn ~ 5825 2675
$EndSCHEMATC
This project is created to detect different types of background radiation
The project is also used to compete during Singapore EIC - 2019 and able to receive merits.


Further details about the project and event : https://www.pressreader.com/philippines/philippine-daily-inquirer-1109/20190826/282157882908504
---------------------------------------------------------------------------------------------------------------------------------------------












NOTES:

Mothercode ---> dapat kaya nya lahat ng required: receive from sensor,
		display on lcd tsaka plot sa webserver.
---------------------------------------------------------------------------------------------------------
Circuit:
VU - (5volts para sa LCD disp, sa VCC nakaconnect)
D0 - 16
D1 - 5 (SCL sa I2C)
D2 - 4 (SDA sa I2C)
D3 - 0
D4 - 2
D5 - 14
D6 - 12 (Dito irereceive yung CPM for gamma)
D7 - 13 (Dito irereceive yung CPM for  beta)
D8 - 15 (Dito irereceive yung CPM for alpha)
---------------------------------------------------------------------------------------------------------
Display mo yung IP sa LCD mga 5 secs tapos clear
 

// Importing modules
import React, {useState} from "react";
import "./App.css";
import Button from '@mui/material/Button';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import Papa from 'papaparse';

function App() {

	const [file, setFile] = useState();
	//object
	const [array, setArray] = useState([]);

	const fileReader = new FileReader();

	/** get the location the file, type and content */
	const handleOnChange = (e) => {
        setFile(e.target.files[0]);
    };

	/** event on submit get the content of the file*/
	const handleOnSubmit = (e) => {
        e.preventDefault();
        if (file) {
            fileReader.onload = function (event) {
                const csvOutput = event.target.result;
				// console.log(csvOutput);
				csvFileToArray(csvOutput);
            };
            fileReader.readAsText(file);
        }
    };

	/** convert the csv content to array of object */
	const csvFileToArray = string => {
		// get the fist line ['Heure', 'Intencite', 'temperature', 'vitesse vent\r']
		const csvHeader = string.slice(0, string.indexOf("\r\n")).split(",");
		// get the other line as array of string ['1h,3A,16C,20km\r', '1h30,2.1A,16C,20km\r',...]
		const csvRowsInit = string.slice(string.indexOf("\n") + 1).split("\n");

		//clear array
		const csvRows = csvRowsInit.filter(e =>  e)

		const array = csvRows.map(i => {
			const values = i.split(",");

			return csvHeader.reduce(
				(object, header, index) =>
				{
			  		object[header] = values[index];
				  	return object;
				},
				{});
		});
		setArray(array);

  };

  const headerKeys = Object.keys(Object.assign({}, ...array));

	return (
		<div className="App">
			<header className="App-header">
				<h1>Import csv file</h1>
				<div>
					<input
						type={"file"}
						id={"csvFileInput"}
						accept={".csv"}
						onChange={handleOnChange}
					/>

					<Button
						variant="contained"
						onClick={(e) => {
							handleOnSubmit(e);
						}}
					>
					IMPORT
					</Button>

					<br/><br/>
					
				  <TableContainer component={Paper}>
					<Table sx={{ minWidth: 650 }} aria-label="simple table">
						<TableHead>
						  <TableRow>
							<TableCell align="right">Heure &nbsp;(H)</TableCell>
							<TableCell align="right">Intensité&nbsp;(A)</TableCell>
							<TableCell align="right">Température du Câble&nbsp;(°C)</TableCell>
							<TableCell align="right">Température Extérieur&nbsp;(°C)</TableCell>
							<TableCell align="right">Vitesse du Vent&nbsp;(Km/h)</TableCell>
						  </TableRow>
						</TableHead>

						<TableBody>
							{array.map((array) => (
							<TableRow key={array.heure} sx={{ '&:last-child td, &:last-child th': { border: 0 } }}>
							  <TableCell align="right">{array.heure}</TableCell>
							  <TableCell align="right">{array.intensite}</TableCell>
							  <TableCell align="right">{array.temperature_ext}</TableCell>
							  <TableCell align="right">{array.temperature_int}</TableCell>
							  <TableCell align="right">{array.vitesseVent}</TableCell>
							</TableRow>
							))}
						</TableBody>
					</Table>
				  </TableContainer>

				</div>
			</header>


		</div>
	);
}

export default App;
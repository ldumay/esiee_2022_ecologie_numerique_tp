// Importing modules
import React, {useEffect, useState} from "react";
import "./App.css";
import Button from '@mui/material/Button';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';

import APIService from "./APIService";
import {deprecate} from "@testing-library/jest-dom/dist/utils";

function App(props) {

	const [file, setFile] = useState();
	//object
	const [array, setArray] = useState([]);
	const [calculatedData, setCalculatedData] = useState([]);


	const fileReader = new FileReader();

	useEffect(()=>{
		fetch("/data").then(response =>
			response.json().then(data => {
				setCalculatedData(data)
				console.log(data)
			})
		);
	},[]);


	const calculate = () =>{
      APIService.SendData(array)
      .then((response) => props.SendData(response))
      .catch(error => console.log('error',error))
    }

	/** get the location the file, type and content */
	const handleOnChange = (e) => {
        setFile(e.target.files[0]);
    };

	// const handleCalculate=(e)=>{
	// 	e.preventDefault();
	// 	calculate();
	// 	}

	/** event on submit get the content of the file*/
	const handleOnSubmit = (e) => {
        e.preventDefault();
        if (file) {
            fileReader.onload = function (event) {
                const csvOutput = event.target.result;
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
		const csvRowsInit = string.slice(string.indexOf("\n") + 1).split("\r\n");

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
								  <TableCell align="right">{array.intensity}</TableCell>
								  <TableCell align="right">{array.temperature_cable}</TableCell>
								  <TableCell align="right">{array.temperature_ambiant}</TableCell>
								  <TableCell align="right">{array.wind_speed}</TableCell>
								</TableRow>
								))}
							</TableBody>
						</Table>
					</TableContainer>

					<Button
						variant="contained"
						// onClick={(e) => {
						// 	handleCalculate(e);
						// }}
						onClick={async () => {
							const response = await fetch("/testapps", {
								method: "POST",
								headers: {
									'Content-Type': 'application/json'
								},
								body: JSON.stringify(array)
							})
							if (response.ok) {
								console.log("it worked")
							}

						}}
					>
						calculate
					</Button>
				</div>
			</header>


		</div>
	);
}

export default App;
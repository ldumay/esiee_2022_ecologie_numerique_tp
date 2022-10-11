// Importing modules
import React, { useState, useEffect } from "react";
import "./App.css";
/* import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper'; */

function App() {
	// usestate for setting a javascript
	// object for storing and using data
	const [data, setdata] = useState({
		name: "",
		age: 0,
		date: "",
		programming: "",
	});

	// Using useEffect for single rendering
	useEffect(() => {
		// Using fetch to fetch the api from
		// flask server it will be redirected to proxy
		fetch("/data").then((res) =>
			res.json().then((data) => {
				// Setting a data from api
				setdata({
					name: data.Name,
					age: data.Age,
					date: data.Date,
					programming: data.programming,
				});
			})
		);
	}, []);

	return (
		<div className="App">
			<header className="App-header">
				<h1>React and flask</h1>
				{/* Calling a data from setdata for showing */}
				<p>{data.name}</p>
				<p>{data.age}</p>
				<p>{data.date}</p>
				<p>{data.programming}</p>

			</header>
{/* 			<body>
				<TableContainer component={Paper}>
					<Table sx={{ minWidth: 650 }} aria-label="simple table">
						<TableHead>
							<TableRow>
								<TableCell>Dessert (100g serving)</TableCell>
								<TableCell align="right">Calories</TableCell>
								<TableCell align="right">Fat&nbsp;(g)</TableCell>
								<TableCell align="right">Carbs&nbsp;(g)</TableCell>
								<TableCell align="right">Protein&nbsp;(g)</TableCell>
							</TableRow>
						</TableHead>
						<TableBody>
							{data.map((data) => (
								<TableRow
									key={data.name}
									sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
								>
									<TableCell component="th" scope="row">
										{data.name}
									</TableCell>
									<TableCell align="right">{data.calories}</TableCell>
									<TableCell align="right">{data.fat}</TableCell>
									<TableCell align="right">{data.carbs}</TableCell>
									<TableCell align="right">{data.protein}</TableCell>
								</TableRow>
							))}
						</TableBody>
					</Table>
				</TableContainer>
			</body> */}
		</div>
	);
}

export default App;

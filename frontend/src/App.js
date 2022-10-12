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
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';

function App() {
	// usestate for setting a javascript
	// object for storing and using data
	const [data, setdata] = useState({
		name: "",
		age: 0,
		date: "",
		programming: "",
	});
	const [file, setFile] = useState();
	const fileReader = new FileReader();

	const handleOnChange = (e) => {
        setFile(e.target.files[0]);
		console.log(e.target.files[0]);
    };

	const handleOnSubmit = (e) => {
        e.preventDefault();

        if (file) {
            fileReader.onload = function (event) {
                const csvOutput = event.target.result;
				console.log(csvOutput);
            };

            fileReader.readAsText(file);
        }
    };


	return (
		<div className="App">

			<header className="App-header">
				<h1>React and flask</h1>
				<form action=''>
					<div>
						<input
							type={"file"}
							id={"csvFileInput"}
							accept={".csv"}
							onChange={handleOnChange}
						/>
					</div>
					<Button
						variant="contained"
						onClick={(e) => {
							handleOnSubmit(e);
						}}
                	>
                    IMPORT CSV
                	</Button>
				</form>

			</header>

			<body>

			</body>
		</div>
	);
}

export default App;

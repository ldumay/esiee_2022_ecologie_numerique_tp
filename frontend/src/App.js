// Importing modules
import React, {useState} from "react";
import "./App.css";
import Button from '@mui/material/Button';

function App() {
	// usestate for setting a javascript
	// object for storing and using data
	// const [data, setdata] = useState({
	// 	Heure: "",
	// 	Intencite: 0,
	// 	temperature: 0,
	// 	vitesse_vent: 0,
	// });

	const [file, setFile] = useState();
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
				csvFileToArray(csvOutput);
            };
            fileReader.readAsText(file);
        }
    };

	/** convert the csv content to array of object */
	const csvFileToArray = string => {
		// get the fist line ['Heure', 'Intencite', 'temperature', 'vitesse vent\r']
		const csvHeader = string.slice(0, string.indexOf("\n")).split(",");
		// get the other line as array of string ['1h,3A,16C,20km\r', '1h30,2.1A,16C,20km\r',...]
		const csvRows = string.slice(string.indexOf("\n") + 1).split("\n");
		// console.log(csvHeader);
		// console.log(csvRows);

		const array = csvRows.map(i => {
			const values = i.split(",");

			return csvHeader.reduce(
				(object, header, index) =>
				{
				  object[header] = values[index];
				  // console.log(object)
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
				</div>
			<br />
				<table>
					<thead>
					  <tr key={"header"}>
						{headerKeys.map((key) => (
						  <th key={key}>{key}</th>
						))}
					  </tr>
					</thead>

					<tbody>
					  {array.map((item,index) => (
						<tr key={index}>
						  {Object.values(item).map((val,itemIndex) => (
							<td key={itemIndex}>{val}</td>
						  ))}
						</tr>
					  ))}
					</tbody>
				</table>
			</header>
		</div>
	);
}

export default App;

import React, { useState } from "react";
import axios from "axios";
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';

function FileUploader() {
  const [file, setFile] = useState(null);
  const [result,setResult] = React.useState('...');

  const UPLOAD_ENDPOINT =
    "http://127.0.0.1:5000/predict";

  const handleSubmit = async e => {
    e.preventDefault();
    //if await is removed, console log will be called before the uploadFile() is executed completely.
    //since the await is added, this will pause here then console log will be called
    let res = await uploadFile(file);
    setResult(res.data)
    console.log(res.data);
  };

  const uploadFile = async file => {
    const formData = new FormData();
    formData.append("avatar", file);
        
    return await axios.post(UPLOAD_ENDPOINT, formData, {
      headers: {
        "Access-Control-Allow-Origin"     : "*",
        "Access-Control-Allow-Credentials": "true",
        "withCredentials" : "true",
        "Access-Control-Allow-Headers"    : "Origin, X-Requested-With, Content-Type, Accept",
        "Access-Control-Allow-Methods"    : "PUT, PATCH, GET, POST, DELETE, OPTION"
      }
    });
  };

  const handleOnChange = e => {
    console.log(e.target.files[0]);
    setFile(e.target.files[0]);
  };

  return (
    <form onSubmit={handleSubmit}>
      <h1  style={{margin:'2.5%'}}>Upload Food Picture</h1>
      <input type="file" onChange={handleOnChange} style={{margin:'2.5%'}} />
      <button type="submit"  style={{margin:'2.5%'}}>Upload File</button>
      <Box
      component="form"
      sx={{
        '& .MuiTextField-root': { m: "2.5%", width: '45%' },
      }}
      noValidate
      autoComplete="off"
    >
      <div>  
        <TextField
          id="outlined-multiline-static"
          label="Output"
          multiline
          rows={10}
          value={result}
        />
      </div>
    </Box>
    </form>
    
    
    
    
  );
  
}

export default FileUploader;


//Modify the UPLOAD_ENDPOINT with the API URL.
//The uploaded file can be retreived via $_FILES['avatar'] on the server-side(PHP).
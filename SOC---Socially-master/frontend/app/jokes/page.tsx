'use client'
import axios from "axios";
import React, { useState } from "react";
import Joke from "./joke";
import Jokes from "./jokes";
import Header from "../components/header";

export default async function Page()
{
    async function onAdd(joke:any, valid:boolean)
    {
        console.log(joke);
        const response = await axios.post("http://localhost:8000/newjoke/", joke);
        console.log(response.data);
        valid = false;
        window.location.reload();

    }
  return(<>
  <Header />
  <Joke  onAdd ={onAdd}/>
  <Jokes />
  </>)
        
        
        
        
}
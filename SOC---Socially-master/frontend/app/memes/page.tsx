'use client'
import axios from "axios";
import React from "react";
import Image from "next/image";
import Header from "../components/header";
import Memes from "./memes";
import Page from "./meme";
import { auth, currentUser } from "@clerk/nextjs";



export default async function Meme()
{

   
    async function onAdd(meme:any, valid:boolean)
    {
        console.log(meme);
        const response = await axios.post("http://localhost:8000/newmeme/", meme);
        console.log(response.data);
        
        valid = false;
        window.location.reload();

    }





    

    return(<> 
    <Header />
    
    <Page onAdd={onAdd} />
    <Memes />
    
    
    </>)

}

import { CldImage ,CldVideoPlayer } from 'next-cloudinary';
import { CldUploadWidget } from 'next-cloudinary';
import { CldUploadButton } from 'next-cloudinary';
import axios from 'axios';
import Header from '../components/header';
import Posts from './posts';

 
 export default async function Home()
 { 
  const res = await axios.get("http://localhost:8000/post/");
  const info = res.data;
  console.log(info);
  console.log(typeof info)
  return(<>
  <Posts info={info} />
  
  
   </>)
  


  


 








 }


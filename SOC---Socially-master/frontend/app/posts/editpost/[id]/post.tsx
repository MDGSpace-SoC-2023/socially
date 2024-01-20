'use client';
import React, { useState } from 'react';
import axios from 'axios';
import { CldUploadWidget } from 'next-cloudinary';

export default function CreatePost( {handleSubmit, post} : {handleSubmit: any, post:any}) {
    const [postData, setPostData] = useState({
        caption: post.caption,
        comments: post.comments,
        likes: post.likes,
        public_url : post.public_url, 
        format : post.format, 
        user: post.user

    });
 
    const handleChange = (e: { target: { name: any; value: any; }; }) => {
        const { name, value } = e.target;
        
        setPostData((prevData) => ({
            ...prevData,
            [name]: value,
        }));
    };

    
    return (<form onSubmit={()=>
        handleSubmit(postData)}>
    <label>
        Caption: 
        <textarea name="caption" value={postData.caption} onChange={handleChange} />
    </label>
    <br />




    <CldUploadWidget
    uploadPreset="my-uploads"
    onSuccess={(result, { widget }) => {
  
    console.log(result.info);
    const public_id = result.info?.public_id;
    const format = result.info?.format;
    setPostData((prevData) => ({
    ...prevData,
    public_id:public_id,
    format:format,
}));
   
   console.log(public_id);
   console.log(format);
   
   widget.close();
  }}
>
  {({ open }) => {
    function handleOnClick() {
      
      open();
    }
    return (
      <button type='button' className='delete-button' onClick={handleOnClick}>
       Change Media 
      </button>
    );
  }}
</CldUploadWidget>
<br/>
<button className='edit-button' type="submit">Create Post</button>
</form>);
        
 

   



};

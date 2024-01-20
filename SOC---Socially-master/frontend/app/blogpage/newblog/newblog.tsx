'use client';
import React, { useState } from 'react';
import axios from 'axios';

export default function CreatePost( {handleSubmit} : {handleSubmit: any}) {
    const [postData, setPostData] = useState({
        type: '',
        title: '',
        content: '',
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
        Type:
        <input type="text" name="type" value={postData.type} onChange={handleChange} />
    </label>
    <br />
    <label>
        Title:
        <input type="text" name="title" value={postData.title} onChange={handleChange} />
    </label>
    <br />
    <label>
        Content:
        <textarea name="content" value={postData.content} onChange={handleChange} />
    </label>
    <br />
    <button type="submit">Create Post</button>
</form>);
        
 

   



       
    };

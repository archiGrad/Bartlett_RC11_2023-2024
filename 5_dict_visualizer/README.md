# construct a json file for the purpose of data visualisation in houdini


reading and processing json file.

houdini python code snippet:
```python

import os

node = hou.pwd()
geo = node.geometry()

import json

# Path to your JSON file
json_file_path = hou.evalParm("json_file")


#make point string attributes
try:
	with open(json_file_path, "r") as f:
	data = json.load(f)

	paragraph = geo.addAttrib(hou.attribType.Point, "paragraph", "")
	film_id = geo.addAttrib(hou.attribType.Point, "film_id", "")
	image_name = geo.addAttrib(hou.attribType.Point, "image_name", "")
	model_path = geo.addAttrib(hou.attribType.Point, "model_path", "")
	image_n = geo.addAttrib(hou.attribType.Point, "image_n", 0)
	time = geo.addAttrib(hou.attribType.Point, "time", 0)
	film_path = geo.addAttrib(hou.attribType.Point, "film_path", "")


	for i, item in enumerate(data["folder"]):
		point = geo.createPoint()
		position = hou.Vector3((i%2)*2,1,i)
		point.setPosition(position)


		paragraph_value = item["paragraph"]
		film_id_value = item["filmID"]
		image_n_value = item["image_n"]
		frame = int(hou.frame())
		image_index = (frame%image_n_value) + 1
		frame_path = os.path.join("$HIP", f"data/fragment_{i}", f"frame_{image_index}.jpg")
		image_name_value = item["image_name"] 


		time_value = item["time"]   
		film_path_value = item["film_path"]

		point.setAttribValue(paragraph, paragraph_value)
		point.setAttribValue(film_id, film_id_value)
		point.setAttribValue(image_name, frame_path)
		point.setAttribValue(image_n, image_n_value)
		point.setAttribValue(time, time_value)
		point.setAttribValue(film_path, film_path_value)

		model_path_value = "$HIP/data/null.obj"
		if item["model_path"] != "":
			model_path_value = os.path.join("$HIP", f"data/fragment_{i+1}/model/{item['model_path']}")
			point.setAttribValue(model_path, model_path_value)
		else:
			point.setAttribValue(model_path, model_path_value)


except FileNotFoundError:
	print(f"File '{json_file_path}' not found.")
except json.JSONDecodeError as e:
	print(f"Error decoding JSON: {e}")

```

storing data in json file
```json
{
	folder": [
	{
		"paragraph": "iDistributed by\nNIPPON HERALD & OFFICE KITANO",
		"filmID": "Dune.mp4",
		"image_name": "frame",
		"model_path": "model.obj",
		"image_n": 25,
		"time": 100,
		"film_path": "Dune Part Two  Official Trailer 3.mp4"
	},
	{
		"paragraph": "In the sands of Arrakis, the fate of civilizations will be decided.",
		"filmID": "Dune.mp4",
		"image_name": "frame",
		"model_path": "",
		"image_n": 15,
		"time": 100,
		"film_path": "Dune Part Two  Official Trailer 3.mp4"
	},
	{
		"paragraph": "A struggle for power and survival unfolds amidst the dunes.",
		"filmID": "Dune.mp4",
		"image_name": "frame",
		"model_path": "",
		"image_n": 30,
		"time": 100,
		"film_path": "Dune Part Two  Official Trailer 3.mp4"
	},
	{
		"paragraph": "The mysterious spice Melange holds the key to control and prosperity.",
		"filmID": "Dune.mp4",
		"image_name": "frame",
		"model_path": "",
		"image_n": 20,
		"time": 100,
		"film_path": "Dune Part Two  Official Trailer 3.mp4"
	},
	...
	]
}
 
```




## end result:
	
	- scene walkthrough with image sequences, subtitles and models	


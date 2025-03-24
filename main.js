function predict() {
  var fileInput = document.getElementById("imageInput");
  var file = fileInput.files[0];
  console.log(file);
  var formData = new FormData();
  formData.append("image", file);

  fetch("http://127.0.0.1:5001/predict", {
    method: "POST",

    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      document.getElementById("result").innerText =
        "Predicted Class: " + data.class;
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

const uploadInput = document.getElementById('fileinput');
const targetInput = document.getElementById('target-input')
const imageContainer = document.getElementById('image-container');
const selectFileBtn = document.getElementById('select-file-btn');
const detectBtn = document.getElementById('detect-btn');
const filenameText = document.getElementById('filename');

console.log(uploadInput);

selectFileBtn.addEventListener('click', () => {
  uploadInput.click();
})

uploadInput.addEventListener('change', () => {
  const file = uploadInput.files[0];
  console.log(file);
  filenameText.textContent = file.name;
  getDataUrl(file).then(dataUrl => {
    displayImage(dataUrl);
  })
});

detectBtn.addEventListener('click', () => {
  target = targetInput.value
  console.log(target)
  detectTarget(target)
    .then(res => res.json())
    .then(res => displayDetectedElement(res))
})

const getDataUrl = (file) => new Promise((resolve, reject) => {
  const reader = new FileReader();
  reader.readAsDataURL(file);
  reader.onload = () => resolve(reader.result);
  reader.onerror = error => reject(error);
})

const displayImage = (dataUrl) => {
  if (imageContainer.firstElementChild) {
    imageContainer.firstElementChild.remove();
  }
  const htmlImg = document.createElement('img');
  htmlImg.src = dataUrl;
  htmlImg.style.height = "100%";
  htmlImg.style.width = "100%";
  const div = document.createElement('div')
  div.style.maxWidth = "100%";
  div.style.maxHeight = "100%";
  div.style.position = "relative";
  div.style.objectFit = "contain";
  div.appendChild(htmlImg)
  imageContainer.appendChild(div);
}

const detectTarget = (target) => {
  console.log('ok')

  const formData = new FormData();
  formData.append('target_img', uploadInput.files[0]);
  console.log(uploadInput.files[0])
  return fetch(`http://localhost:5000/detect/${target}`, {
    method: 'POST',
    credentials: 'same-origin',
    body: formData
  });
}

const displayDetectedElement = (data) => {
  const img = imageContainer.firstElementChild
  console.log(data)
  data.fetchedCoords
    .map(el => {
      console.log(el)
      return getElementStyle({width: img.offsetWidth, height: img.offsetHeight}, el, data.imgWidth, data.imgHeight);
    })
    .forEach(elStyle => {
      const htmlEl = document.createElement('div');
      htmlEl.style.position = 'absolute';
      htmlEl.style.top = elStyle.top;
      htmlEl.style.left = elStyle.left;
      htmlEl.style.width = elStyle.width;
      htmlEl.style.height = elStyle.height;
      htmlEl.style.border = 'solid green 2px';
      imageContainer.firstElementChild.appendChild(htmlEl);
    });
}

const getElementStyle = (imgStyle, element, imgWidth, imgHeight) => {
  console.log(imgStyle)
  return {
    width: (imgStyle.width * element.width / imgWidth) + 'px',
    height: (imgStyle.height * element.height / imgHeight) + 'px',
    top: (element.top * imgStyle.height / imgHeight) + 'px',
    left: (element.left * imgStyle.width / imgWidth) + 'px'
  }
}

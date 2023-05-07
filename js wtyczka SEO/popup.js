let tagCount = {};

function updateTagCount() {
  chrome.tabs.executeScript(
    {
      code: `
      const tagH1 = document.querySelectorAll("h1");
      const tagH2 = document.querySelectorAll("h2");
      const tagH3 = document.querySelectorAll("h3");
      const tagH4 = document.querySelectorAll("h4");
      const tagH5 = document.querySelectorAll("h5");
      const tagH6 = document.querySelectorAll("h6");
      const imgCount = document.querySelectorAll("img");

      const tagCount = {
        h1: tagH1.length,
        h2: tagH2.length,
        h3: tagH3.length,
        h4: tagH4.length,
        h5: tagH5.length,
        h6: tagH6.length,
        img: imgCount.length,
        imgBezAlt: countImgBezAlt(),
        charCount: document.querySelector('body').innerText.length,
        loadSpeed: window.performance.timing.domContentLoadedEventEnd - window.performance.timing.navigationStart
      };

      function h1in() {
        let h1Inner = '';
        for(let i = 0; i < tagH1.length; i++) {
          h1Inner += '<p>' + tagH1[i].innerText + '</p>'
        }
      }

      function countImgBezAlt() {
        let count = 0;
        const images = document.querySelectorAll('img:not([alt])');
        for (let i = 0; i < images.length; i++) {
          count++;
        }
        return count;
      }

      tagCount;
    `,
    },
    function (result) {
      tagCount = result[0];

      const tagCountElement = document.getElementById("tag-count");
      
      tagCountElement.innerHTML = `
        <p>H1: ${tagCount.h1}</p>
        <p>H2: ${tagCount.h2}</p>
        <p>H3: ${tagCount.h3}</p>
        <p>H4: ${tagCount.h4}</p>
        <p>H5: ${tagCount.h5}</p>
        <p>H6: ${tagCount.h6}</p>
        <p>IMG: ${tagCount.img}</p>
        <p>IMG bez alt: ${tagCount.imgBezAlt}</p>
        <p>Liczba znaków: ${tagCount.charCount}</p>
        <p>Szybkość ładowania: ${tagCount.loadSpeed}ms</p>
      `;
    }
  );
}

document.addEventListener("DOMContentLoaded", function () {
  updateTagCount();
});

chrome.tabs.onActivated.addListener(function (activeInfo) {
  updateTagCount();
});

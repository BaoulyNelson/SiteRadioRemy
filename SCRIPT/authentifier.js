// <type="module">
// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.11.1/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.11.1/firebase-analytics.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyAun8nHlFnWm_P-1wp4viasQEziYSzez-c",
  authDomain: "mfmradio-91f78.firebaseapp.com",
  projectId: "mfmradio-91f78",
  storageBucket: "mfmradio-91f78.appspot.com",
  messagingSenderId: "315069388258",
  appId: "1:315069388258:web:2f47a33beab816fa8dd5bb",
  measurementId: "G-68ZR0G3GQJ"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

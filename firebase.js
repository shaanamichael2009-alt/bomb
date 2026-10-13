import { initializeApp } from "firebase/app";
import { getFirestore } from "firebase/firestore";
import { getStorage } from "firebase/storage";

const firebaseConfig = {
  apiKey: "AIzaSyCPbwGqF7-Z55_cESld9pBUe_zsrtF002E",
  authDomain: "gift-card-val.firebaseapp.com",
  projectId: "gift-card-val",
  storageBucket: "gift-card-val.firebasestorage.app",
  messagingSenderId: "994306585676",
  appId: "1:994306585676:web:3b6e52d77f43ea91ab30e9"
};

const app = initializeApp(firebaseConfig);
export const db = getFirestore(app);
export const storage = getStorage(app);
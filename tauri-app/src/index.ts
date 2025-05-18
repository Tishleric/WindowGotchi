import { invoke } from "@tauri-apps/api/tauri";
import { Pet, PetState } from "./pet";

const statusEl = document.getElementById("status") as HTMLElement;
const feedBtn = document.getElementById("feed") as HTMLButtonElement;

let pet = new Pet();

async function load() {
  const state = (await invoke("get_state")) as PetState;
  Object.assign(pet, state);
  render();
}

async function save() {
  await invoke("set_state", { newState: pet });
}

function render() {
  statusEl.textContent = JSON.stringify(pet, null, 2);
}

feedBtn.addEventListener("click", async () => {
  pet.feed("snack");
  render();
  await save();
});

load();

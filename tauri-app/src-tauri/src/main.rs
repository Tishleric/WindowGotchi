#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

use serde::{Deserialize, Serialize};
use std::sync::Mutex;
use tauri::State;

#[derive(Debug, Serialize, Deserialize, Clone)]
struct PetState {
    age_minutes: u32,
    stage: String,
    hunger_hearts: u8,
    happiness_hearts: u8,
    discipline_percent: u8,
    weight: u8,
    care_mistakes: u8,
    is_sick: bool,
    poop_count: u8,
}

impl Default for PetState {
    fn default() -> Self {
        Self {
            age_minutes: 0,
            stage: "Baby".into(),
            hunger_hearts: 4,
            happiness_hearts: 4,
            discipline_percent: 0,
            weight: 5,
            care_mistakes: 0,
            is_sick: false,
            poop_count: 0,
        }
    }
}

struct AppState(Mutex<PetState>);

#[tauri::command]
fn get_state(state: State<AppState>) -> PetState {
    state.0.lock().unwrap().clone()
}

#[tauri::command]
fn set_state(new_state: PetState, state: State<AppState>) {
    *state.0.lock().unwrap() = new_state;
}

fn main() {
    tauri::Builder::default()
        .manage(AppState(Mutex::new(PetState::default())))
        .invoke_handler(tauri::generate_handler![get_state, set_state])
        .run(tauri::generate_context!())
        .expect("failed to run tauri application");
}

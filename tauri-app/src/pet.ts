export enum Stage {
  BABY = "Baby",
  CHILD = "Child",
  TEEN = "Teen",
  ADULT = "Adult",
  DEAD = "Dead",
}

export interface PetState {
  age_minutes: number;
  stage: Stage;
  hunger_hearts: number;
  happiness_hearts: number;
  discipline_percent: number;
  weight: number;
  care_mistakes: number;
  is_sick: boolean;
  poop_count: number;
}

export class Pet implements PetState {
  age_minutes = 0;
  stage = Stage.BABY;
  hunger_hearts = 4;
  happiness_hearts = 4;
  discipline_percent = 0;
  weight = 5;
  care_mistakes = 0;
  is_sick = false;
  poop_count = 0;

  private minutes_since_last_hunger = 0;
  private minutes_since_last_happy = 0;
  private minutes_since_last_poop = 0;

  tick(minutes = 1): void {
    for (let i = 0; i < minutes; i++) {
      this.age_minutes++;
      this.minutes_since_last_hunger++;
      this.minutes_since_last_happy++;
      this.minutes_since_last_poop++;

      if (this.minutes_since_last_hunger >= 60) {
        if (this.hunger_hearts > 0) this.hunger_hearts--;
        this.minutes_since_last_hunger = 0;
        if (this.hunger_hearts === 0) this.care_mistakes++;
      }

      if (this.minutes_since_last_happy >= 70) {
        if (this.happiness_hearts > 0) this.happiness_hearts--;
        this.minutes_since_last_happy = 0;
        if (this.happiness_hearts === 0) this.care_mistakes++;
      }

      if (this.minutes_since_last_poop >= 180) {
        this.poop_count++;
        this.minutes_since_last_poop = 0;
      }

      this.maybeEvolve();
    }
  }

  feed(foodType: "meal" | "snack"): boolean {
    if (foodType === "meal") {
      if (this.hunger_hearts >= 4) return false;
      this.hunger_hearts++;
      this.weight++;
      return true;
    }
    if (foodType === "snack") {
      if (this.happiness_hearts < 4) this.happiness_hearts++;
      this.weight += 2;
      if (this.weight > 20) this.is_sick = true;
      return true;
    }
    return false;
  }

  playGame(roundsWon: number): void {
    if (roundsWon >= 3 && this.happiness_hearts < 4) this.happiness_hearts++;
    if (this.weight > 1) this.weight--;
  }

  cleanPoop(): void {
    this.poop_count = 0;
  }

  giveMedicine(): void {
    if (this.is_sick) this.is_sick = false;
  }

  discipline(): void {
    this.discipline_percent = Math.min(100, this.discipline_percent + 25);
  }

  private maybeEvolve(): void {
    if (this.stage === Stage.BABY && this.age_minutes >= 65) {
      this.stage = Stage.CHILD;
    } else if (this.stage === Stage.CHILD && this.age_minutes >= 3 * 24 * 60) {
      this.stage = Stage.TEEN;
    } else if (this.stage === Stage.TEEN && this.age_minutes >= 6 * 24 * 60) {
      this.stage = Stage.ADULT;
    }
  }
}

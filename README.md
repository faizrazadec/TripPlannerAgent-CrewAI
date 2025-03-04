# **Trip Planning Agent using CrewAI**  

## **Introduction**  
The **Trip Planner Agent** is a powerful tool built on top of the **CrewAI** framework, designed to assist travelers in planning and scheduling their trips. This project showcases how CrewAI automates the decision-making process when travelers are uncertain about their destination choices. By leveraging a team of autonomous AI agents, CrewAI enables seamless collaboration to analyze different options and generate an optimized travel itinerary tailored to user preferences.  

## **CrewAI Framework**  
[CrewAI](https://www.crewai.com/) is designed to facilitate intelligent collaboration between role-based AI agents. In this project, these agents work together to assess various cities, compare travel conditions, and craft a well-structured itinerary that aligns with the traveler's preferences and budget.  

## **Prerequisites**  
- Python 3.8 or later  
- Access to **gpt-4o-mini** (default model used)  
- OpenAI API key  
- Required dependencies (listed in `requirements.txt`)  

⚠️ **Disclaimer:** This script defaults to **gpt-4o-mini** unless modified, which may incur usage costs.  

---

## **Getting Started**  

### **1. Clone the Repository**  
```bash
git clone https://github.com/faizrazadec/TripPlannerAgent-CrewAI.git
cd TripPlannerAgent-CrewAI
```

### **2. Set Up a Virtual Environment**  
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### **3. Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **4. Configure API Keys**  
Create a `.env` file in the project directory and add your OpenAI API key:  
```
OPENAI_API_KEY=your_api_key_here
SERPER_API_KEY=your_api_key_here
```

### **5. Run the Application**  
```bash
python3 main.py
```

---

## **Project Structure**  
📂 **trip-planner-agent/**  
│── 📄 `main.py` – Main script to run the trip planner  
│── 📄 `trip_tasks.py` – Defines task prompts and execution logic  
│── 📄 `trip_agents.py` – Handles agent creation and behavior  
│── 📂 `tools/` – Custom tools and utilities used by agents  
│── 📄 `requirements.txt` – Lists dependencies for installation  

---

## **How It Works**  
1. **Input Your Preferences**: Specify your preferred travel dates, budget, and destination options.  
2. **Autonomous Agent Collaboration**: CrewAI agents will analyze weather conditions, seasonal trends, and cost factors to determine the best city for your trip.  
3. **Generate a Custom Itinerary**: The AI will compile an optimized travel plan, including recommended activities, accommodations, and budget breakdowns.  

---

## **Example Travel Itinerary Generated**  

### **7-Day Travel Itinerary: Islamabad, Lahore, and Karachi (August 5th - August 12th, 2025)**  

### **Day 1: Arrival in Islamabad (August 5th, 2025)**  
- **Morning:**  
  - Arrive at Islamabad International Airport.  
  - Transfer to **Islamabad Serena Hotel** (5-star) [$150/night].  
- **Afternoon:**  
  - Visit **Faisal Mosque**.  
- **Evening:**  
  - Dinner at **The Carnivore** for Turkish cuisine.  
- **Weather:** Hot and humid, average 35°C (95°F).  
- **Pack:** Light clothing, hat, sunscreen.  
- **Estimated Budget:**  
  - Hotel: $150  
  - Meals: $25  
  - Transportation: $10  
  - **Total:** $185  

### **Day 2: Explore Islamabad (August 6th, 2025)**  
- **Morning:**  
  - Breakfast at hotel.  
  - Visit **Pakistan Monument**.  
- **Afternoon:**  
  - Lunch at **Dawat** [Pakistani].  
  - Explore **Lok Virsa Museum**.  
- **Evening:**  
  - Free time at **Shahbaz Sharif Park**.  
  - Dinner at local cafe in **Saddar Market**.  
- **Weather:** High of 38°C (100°F).  
- **Pack:** Comfortable shoes, lightweight layers.  
- **Estimated Budget:**  
  - Meals: $30  
  - Entrance Fees: $5  
  - **Total:** $35  

### **Day 3: Travel to Lahore (August 7th, 2025)**  
- **Morning:**  
  - Early breakfast and check out.  
  - Travel to Lahore via flight [$80].  
- **Afternoon:**  
  - Check in at **Pearl Continental Lahore** [$140/night].  
  - Lunch at **Andaaz Restaurant**.  
- **Evening:**  
  - Visit **Badshahi Mosque**.  
- **Weather:** Average 36°C (97°F).  
- **Pack:** Modest clothing for mosques.  
- **Estimated Budget:**  
  - Hotel: $140  
  - Meals: $35  
  - Flight: $80  
  - **Total:** $255  

### **Day 4: Discover Lahore (August 8th, 2025)**  
- **Morning:**  
  - Breakfast at hotel.  
  - Visit **Lahore Fort** [UNESCO site].  
- **Afternoon:**  
  - Lunch at **Bistro at Nishat Hotels**.  
  - Stroll through **Shalimar Gardens**.  
- **Evening:**  
  - Dinner at **Café Zouk**, known for its lively atmosphere.  
- **Weather:** High of 37°C (99°F).  
- **Pack:** Casual attire, a reusable water bottle.  
- **Estimated Budget:**  
  - Meals: $40  
  - Entrance Fees: $5  
  - **Total:** $45  

### **Day 5: Travel to Karachi (August 9th, 2025)**  
- **Morning:**  
  - Breakfast and check out.  
  - Fly to Karachi [$80].  
- **Afternoon:**  
  - Check in at **Mövenpick Hotel Karachi** [$150/night].  
  - Visit **Quaid-e-Azam’s Mausoleum**.  
- **Evening:**  
  - Dinner at **The Deli** in Mövenpick.  
- **Weather:** Average 34°C (93°F).  
- **Pack:** Beachwear and lightweight clothing.  
- **Estimated Budget:**  
  - Hotel: $150  
  - Meals: $30  
  - Flight: $80  
  - **Total:** $260  

### **Day 6: Relax and Explore Karachi (August 10th, 2025)**  
- **Morning:**  
  - Breakfast at hotel.  
  - Relax at **Clifton Beach**.  
- **Afternoon:**  
  - Lunch at a local street stall - **Bun Kebab**.  
  - Visit **Frere Hall** and gardens.  
- **Evening:**  
  - Dinner at **Chai Shai** for late-night chai vibes.  
- **Weather:** High of 36°C (97°F).  
- **Pack:** Swim gear and towels for the beach.  
- **Estimated Budget:**  
  - Meals: $25  
  - Beach activities: $5  
  - **Total:** $30  

### **Day 7: Departure (August 11th, 2025)**  
- **Morning:**  
  - Breakfast at hotel and check out.  
  - Last-minute shopping and exploring in **Dolmen Mall Clifton**.  
- **Afternoon:**  
  - Departure for Islamabad International Airport for your flight back to Berlin.  
- **Weather:** Average 33°C (91°F).  
- **Pack:** Something formal for travel day.  
- **Estimated Budget:**  
  - Meals: $20  
  - Transfers: $15  
  - **Total:** $35  

---

## **Total Budget Breakdown**  
- **Flights (Berlin to Islamabad and back):** $855  
- **Intra-country Flights:** $160  
- **Accommodation:** $1,050  
- **Meals (Estimated):** $280  
- **Attractions & Transport:** $75  
- **Total Estimated Costs:** **$2,420**  

---

## **Packing Suggestions**  
- Light, breathable clothing that can be layered.  
- Modest attire for mosque visits.  
- Sunscreen, hat, and sunglasses.  
- Comfortable walking shoes.  
- Swimwear for beach days.  

🚀 **Start planning your dream trip today with AI-powered efficiency!**

import streamlit as st

st.title("Support of Daily Living Function")

# Mapping of original SST means (Column A) to updated community services (Column B)
sst_mapping = {
    "Assisted living (e.g. group home, serviced apartment)": [
        "Sheltered home", "Destitute home", "Adult disable home"
    ],
    "Family or friend (close by)": [
        "Family or friend (close by)"
    ],
    "Family or friend (not close by)": [
        "Family or friend (not close by)"
    ],
    "Foreign Domestic Worker (trained as a caregiver)": [
        "Foreign Domestic Worker (trained as a caregiver)"
    ],
    "High level center based care (e.g. Day Rehabilitation, Dementia day care, SPICE)": [
        "Day care", "Dementia day care", "Day hospice care", "Day rehabilitation",
        "Centre-based nursing", "Night respite", "Geriatric day hospital"
    ],
    "IT solution not requiring human support (e.g. robotic healthcare assistant)": [
        "Red Cross Home Monitoring and Eldercare (HoME+)"
    ],
    "IT solution requiring human support (e.g. telemedicine)": [
        "CGH Health Management Unit (tele-education)"
    ],
    "Lay Volunteer (e.g. befrienders, pastor, NHG Neighbours)": [
        "CGH Neighbours", "AIC befriending service", "Health peers", "Montfort Care befriending"
    ],
    "Low level center based care (e.g. Senior Activity Center, community centers, program based centers, MSF funded centers)": [
        "Community rehabilitation centre", "Maintenance day care centre", "Respite care",
        "Senior activity centre (AIC)", "Senior day care", "Community health post",
        "Community psychiatric programme (CGPP)", "Eastern community hospital at home (EchH)",
        "Our Silvercare Hub (OSH)"
    ],
    "Multidisciplinary team (e.g. COMIT (AIC Community Intervention Team), Transitional Care)": [
        "Community intervention team (COMIT)", "Community outreach teams (CREST)",
        "Geriatric day hospital (GDH)", "EAGLECare programme", "CGH@Home", "CGH Frail To Fit clinic"
    ],
    "Nurse (e.g. community/inpatient/outpatient nurse)": [
        "Home nursing", "Centre-based nursing", "Community nursing"
    ],
    "Nursing home": [
        "Nursing home", "EAGLECare Programme (Salvation Army Peacehaven Nursing Home)",
        "Moral Home for the Aged Sick", "Lions Home for the Elders",
        "NTUC Health Chai Chee Nursing Home", "All Saints Home Tampines"
    ],
    "Paid home care aide (e.g. paid IADL services such as grocery/meals delivery, house keeping, grooming, supervision, etc)": [
        "Home Personal Care (HPC)", "Meals-On-Wheels (MOW)", "Medical Escort and Transport (MET)",
        "Interim caregiver service (ICS)"
    ],
    "Support group (e.g. religious, disease/condition specific, clan, People’s Association, Samaritans of Singapore, Community Network for Seniors, Senior Citizen’s Support Groups)": [
        "Samaritans of Singapore", "Stroke support station", "SA Dehda",
        "Parkinson Society Singapore support group", "Diabetes support group",
        "CGH Medical Social Service (MSS)", "CGH Medical Social Worker (MSW)"
    ]
}

# Render expanders with checkboxes
for category, options in sst_mapping.items():
    with st.expander(category, expanded=False):
        for item in options:
            st.checkbox(item, key=f"{category}_{item}")

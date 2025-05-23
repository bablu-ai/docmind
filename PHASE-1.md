
%%{
  init: {
    'theme': 'base',
    'themeVariables': {
      'fontFamily': 'Comic Sans MS, cursive',
      'fontSize': '16px',
      'primaryColor': '#FDFD96',        # Light Yellow
      'nodeBorder': '#383838',
      'lineColor': '#555',
      'primaryTextColor': '#333',
      'secondaryColor': '#ADD8E6',      # Light Blue
      'tertiaryColor': '#FFB347'       # Light Orange
    }
  }
}%%
graph TD;
    %% Define Stylesa
    classDef userStyle fill:#C1E1C1,stroke:#508050,stroke-width:2px;  %% Light Green
    classDef uiStyle fill:#ADD8E6,stroke:#5A9FB8,stroke-width:2px;     %% Light Blue
    classDef backendStyle fill:#FDFD96,stroke:#B8B84E,stroke-width:2px; %% Light Yellow
    classDef llmStyle fill:#FFB347,stroke:#B87A30,stroke-width:2px;     %% Light Orange

    %% Define Nodes and Subgraphs
    User([User]):::userStyle;

    subgraph Frontend
        direction LR
        UI[Chat Interface]:::uiStyle;
    end

    subgraph Backend
        direction LR
        BackendService[Backend API Service]:::backendStyle;
    end

    LLM[Large Language Model API]:::llmStyle;

    %% Define Flow
    User -- Query --> UI;
    UI -- Sends Query --> BackendService;
    BackendService -- Calls LLM --> LLM;
    LLM -- Returns Response --> BackendService;
    BackendService -- Sends Response --> UI;
    UI -- Displays Response --> User;

    %% Apply curved lines if supported well by renderer
    linkStyle default interpolate basis
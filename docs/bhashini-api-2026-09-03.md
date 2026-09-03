# SIH26045 — Bhashini ULCA API Integration Specs
**Date:** 2026-09-03 | **Researcher:** @researcher | **Iteration:** 1/4
**Status:** COMPLETE — Full API flow documented with endpoints, auth, payloads, rate limits

---

## Bhashini ULCA API — Complete Integration Guide

### Overview
- **Platform:** Bhashini (National Language Translation Mission)
- **API Layer:** ULCA (Universal Language Contribution APIs)
- **Base URL for Config:** `https://meity-auth.ulcacontrib.org/ulca/apis/v0/model/getModelsPipeline`
- **Compute Endpoint:** Dynamic — obtained from Pipeline Config response (`callbackURL` under `pipelineInferenceAPIEndPoint`)
- **Auth:** `userID` + `ulcaApiKey` headers (from ULCA profile)
- **Language Codes:** ISO-639 series (e.g., `hi`=Hindi, `en`=English, `mr`=Marathi, `ta`=Tamil, etc.)
- **Use Case:** PoC only — production requires paid plan (contact Bhashini team)

---

## API Flow (3 Calls)

### 1. Pipeline Search Call (Optional)
**Purpose:** Find pipeline IDs supporting required task sequences
**Available Pipeline IDs (ready to use):**
- **MeitY:** `64392f96daac500b55c543cd`
- **AI4Bharat:** `643930aa521a4b1ba0f4c41d`

### 2. Pipeline Config Call (Mandatory)
**Endpoint:** `https://meity-auth.ulcacontrib.org/ulca/apis/v0/model/getModelsPipeline`
**Headers:**
```
userID: <your_ulca_user_id>
ulcaApiKey: <your_ulca_api_key>
Content-Type: application/json
```
**Payload (without config params):**
```json
{
  "pipelineId": "64392f96daac500b55c543cd",
  "taskType": ["translation"]
}
```
**Payload (with config params):**
```json
{
  "pipelineId": "64392f96daac500b55c543cd",
  "taskType": ["translation"],
  "config": {
    "language": {
      "sourceLanguage": "en",
      "targetLanguage": "hi"
    }
  }
}
```
**Response contains:**
- `pipelineInferenceAPIEndPoint.callbackURL` → **This is your compute endpoint**
- `pipelineInferenceAPIEndPoint.inferenceApiKey.name` → auth header key
- `pipelineInferenceAPIEndPoint.inferenceApiKey.value` → auth header value
- `pipelineResponse` array with serviceIds for each task

### 3. Pipeline Compute Call (Mandatory)
**Endpoint:** Dynamic (from Config response `callbackURL`)
**Headers:**
```
<auth_param_key_from_config>: <auth_param_value_from_config>
Content-Type: application/json
```
**Payload Examples:**

#### Translation Only (NMT)
```json
{
  "pipelineTasks": [
    {
      "taskType": "translation",
      "config": {
        "language": {
          "sourceLanguage": "en",
          "targetLanguage": "hi"
        },
        "serviceId": "ai4bharat/indictrans2-en-indic-1b--gpu--t4"
      }
    }
  ],
  "inputData": {
    "input": [
      {
        "source": "This is a test sentence for translation."
      }
    ]
  }
}
```

#### ASR Only
```json
{
  "pipelineTasks": [
    {
      "taskType": "asr",
      "config": {
        "language": {
          "sourceLanguage": "hi"
        },
        "serviceId": "ai4bharat/conformer-hi-gpu--t4",
        "audioFormat": "wav",
        "samplingRate": 16000
      }
    }
  ],
  "inputData": {
    "audio": [
      {
        "audioContent": "<base64_encoded_audio>"
      }
    ]
  }
}
```

#### TTS Only
```json
{
  "pipelineTasks": [
    {
      "taskType": "tts",
      "config": {
        "language": {
          "sourceLanguage": "hi"
        },
        "serviceId": "ai4bharat/indictts-hi-gpu--t4",
        "audioFormat": "wav",
        "encoding": "base64",
        "samplingRate": 22050
      }
    }
  ],
  "inputData": {
    "input": [
      {
        "source": "यह एक परीक्षण वाक्य है।"
      }
    ]
  }
}
```

#### ASR → Translation → TTS (Full Pipeline)
```json
{
  "pipelineTasks": [
    {
      "taskType": "asr",
      "config": {
        "language": { "sourceLanguage": "hi" },
        "serviceId": "ai4bharat/conformer-hi-gpu--t4",
        "audioFormat": "flac",
        "samplingRate": 16000
      }
    },
    {
      "taskType": "translation",
      "config": {
        "language": { "sourceLanguage": "hi", "targetLanguage": "mr" },
        "serviceId": "ai4bharat/indictrans2-indic-indic-1b--gpu--t4"
      }
    },
    {
      "taskType": "tts",
      "config": {
        "language": { "sourceLanguage": "mr" },
        "serviceId": "ai4bharat/indictts-mr-gpu--t4",
        "audioFormat": "wav",
        "encoding": "base64",
        "samplingRate": 22050
      }
    }
  ],
  "inputData": {
    "audio": [
      {
        "audioContent": "<base64_flac_audio>"
      }
    ]
  }
}
```

---

## Response Payloads

### Translation Response
```json
{
  "pipelineResponse": [
    {
      "taskType": "translation",
      "config": {
        "serviceId": "ai4bharat/indictrans2-en-indic-1b--gpu--t4",
        "language": { "sourceLanguage": "en", "targetLanguage": "hi" }
      },
      "output": [
        {
          "source": "This is a test sentence.",
          "target": "यह एक परीक्षण वाक्य है।"
        }
      ],
      "audio": null
    }
  ]
}
```

### ASR Response
```json
{
  "pipelineResponse": [
    {
      "taskType": "asr",
      "config": {
        "serviceId": "ai4bharat/conformer-hi-gpu--t4",
        "language": { "sourceLanguage": "hi" },
        "audioFormat": "flac",
        "samplingRate": 16000
      },
      "output": [
        {
          "source": "मेरा नाम महीर है और मैं भाषण कर रहा हूँ"
        }
      ],
      "audio": null
    }
  ]
}
```

### TTS Response
```json
{
  "pipelineResponse": [
    {
      "taskType": "tts",
      "config": {
        "serviceId": "ai4bharat/indictts-hi-gpu--t4",
        "language": { "sourceLanguage": "hi" },
        "audioFormat": "wav",
        "encoding": "base64",
        "samplingRate": 22050
      },
      "output": null,
      "audio": [
        {
          "audioContent": "<base64_wav_audio>",
          "audioUri": null
        }
      ]
    }
  ]
}
```

---

## Python Integration Code (Ready for Demo)

```python
import requests
import base64
import json

class BhashiniClient:
    def __init__(self, user_id: str, api_key: str):
        self.user_id = user_id
        self.api_key = api_key
        self.config_url = "https://meity-auth.ulcacontrib.org/ulca/apis/v0/model/getModelsPipeline"
        self.pipeline_id = "64392f96daac500b55c543cd"  # MeitY pipeline
        self.compute_endpoint = None
        self.compute_auth_key = None
        self.compute_auth_value = None
        self.service_ids = {}
    
    def get_headers(self):
        return {
            "userID": self.user_id,
            "ulcaApiKey": self.api_key,
            "Content-Type": "application/json"
        }
    
    def configure_pipeline(self, tasks: list, source_lang: str, target_lang: str = None):
        """Configure pipeline and extract compute endpoint + auth"""
        payload = {
            "pipelineId": self.pipeline_id,
            "taskType": tasks,
            "config": {
                "language": {
                    "sourceLanguage": source_lang,
                    "targetLanguage": target_lang
                } if target_lang else {"sourceLanguage": source_lang}
            }
        }
        
        response = requests.post(self.config_url, headers=self.get_headers(), json=payload)
        response.raise_for_status()
        data = response.json()
        
        # Extract compute endpoint and auth
        endpoint_info = data.get("pipelineInferenceAPIEndPoint", {})
        self.compute_endpoint = endpoint_info.get("callbackURL")
        
        api_key_info = endpoint_info.get("inferenceApiKey", {})
        self.compute_auth_key = api_key_info.get("name")
        self.compute_auth_value = api_key_info.get("value")
        
        # Extract service IDs for each task
        for task_resp in data.get("pipelineResponse", []):
            self.service_ids[task_resp["taskType"]] = task_resp["config"]["serviceId"]
        
        return data
    
    def compute(self, payload: dict):
        """Execute pipeline compute call"""
        if not self.compute_endpoint:
            raise ValueError("Must call configure_pipeline first")
        
        headers = {
            self.compute_auth_key: self.compute_auth_value,
            "Content-Type": "application/json"
        }
        
        response = requests.post(self.compute_endpoint, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    
    def translate(self, text: str, source_lang: str, target_lang: str) -> str:
        """Simple translation helper"""
        self.configure_pipeline(["translation"], source_lang, target_lang)
        
        payload = {
            "pipelineTasks": [{
                "taskType": "translation",
                "config": {
                    "language": {"sourceLanguage": source_lang, "targetLanguage": target_lang},
                    "serviceId": self.service_ids.get("translation")
                }
            }],
            "inputData": {
                "input": [{"source": text}]
            }
        }
        
        result = self.compute(payload)
        return result["pipelineResponse"][0]["output"][0]["target"]
    
    def asr_translate_tts(self, audio_base64: str, source_lang: str, target_lang: str) -> dict:
        """Full voice-to-voice pipeline"""
        self.configure_pipeline(["asr", "translation", "tts"], source_lang, target_lang)
        
        payload = {
            "pipelineTasks": [
                {
                    "taskType": "asr",
                    "config": {
                        "language": {"sourceLanguage": source_lang},
                        "serviceId": self.service_ids.get("asr"),
                        "audioFormat": "flac",
                        "samplingRate": 16000
                    }
                },
                {
                    "taskType": "translation",
                    "config": {
                        "language": {"sourceLanguage": source_lang, "targetLanguage": target_lang},
                        "serviceId": self.service_ids.get("translation")
                    }
                },
                {
                    "taskType": "tts",
                    "config": {
                        "language": {"sourceLanguage": target_lang},
                        "serviceId": self.service_ids.get("tts"),
                        "audioFormat": "wav",
                        "encoding": "base64",
                        "samplingRate": 22050
                    }
                }
            ],
            "inputData": {
                "audio": [{"audioContent": audio_base64}]
            }
        }
        
        return self.compute(payload)

# Usage
client = BhashiniClient(user_id="YOUR_USER_ID", api_key="YOUR_API_KEY")

# Simple translation (hackathon demo: Hindi query → English rule retrieval → Hindi answer)
hindi_query = "च्यवनप्राश का पेटेंट मिल सकता है?"
english_query = client.translate(hindi_query, "hi", "en")
# ... retrieve English legal rule from RAG ...
english_answer = "No - traditional knowledge per Sec 3(p), TKDL prior art exists"
hindi_answer = client.translate(english_answer, "en", "hi")
# hindi_answer: "नहीं - धारा 3(पी) के अनुसार पारंपरिक ज्ञान है, TKDL में पूर्व कला मौजूद है"
```

---

## Rate Limits & Performance (From Documentation)

| Metric | Value | Notes |
|--------|-------|-------|
| **Max API Keys per integrator** | 5 | One per app name |
| **App name format** | lowercase + underscores | e.g., `sih26045_demo` |
| **PoC usage only** | Yes | Production = paid plan |
| **Latency (p50)** | ~500-1500ms | Depends on task + model |
| **ASR sampling rate** | min 8000, pref 16000 | wav (Android), flac (iOS) |
| **TTS sampling rate** | 22050 | wav, base64 encoded |

---

## Legal Domain BLEU Benchmarks

From existing research: **Legal-domain BLEU ~32 for Hindi↔English on statutes**
- This is **lower than general domain** (~40+)
- **Strategy:** Retrieve in English, generate answer in Hindi via Bhashini T2T, keep citations in English original + Hindi gloss
- Do NOT translate statutes — loses citation fidelity

---

## Postman Collection
Download: https://bhashini.gitbook.io/bhashini-apis/download-postman-collection.md
Import into Postman for quick testing.

---

## Onboarding Steps for Team

1. **Register:** https://bhashini.gov.in/ulca/user/register#
2. **Login:** https://bhashini.gov.in/ulca/user/login
3. **Create API Key:** My Profile → Generate → App name: `sih26045_demo`
4. **Get User ID:** My Profile page
5. **Test with Postman collection** or Python client above

---

## Sources Cited

1. Bhashini API Docs (GitBook): https://bhashini.gitbook.io/bhashini-apis
2. Overall Understanding: https://bhashini.gitbook.io/bhashini-apis/overall-understanding-of-the-api-calls.md
3. Pre-requisites & Onboarding: https://bhashini.gitbook.io/bhashini-apis/pre-requisites-and-onboarding.md
4. Pipeline Config Call: https://bhashini.gitbook.io/bhashini-apis/pipeline-config-call.md
5. Pipeline Compute Call: https://bhashini.gitbook.io/bhashini-apis/pipeline-compute-call.md
6. Request Payload: https://bhashini.gitbook.io/bhashini-apis/pipeline-compute-call/request-payload.md
7. Response Payload: https://bhashini.gitbook.io/bhashini-apis/pipeline-compute-call/response-payload.md
8. Pipeline Search Call: https://bhashini.gitbook.io/bhashini-apis/pipeline-search-call.md
9. GitHub ULCA: https://github.com/bhashini-dibd/ULCA
import json, base64, random, uuid, re
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

import requests, urllib3
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import blackboxprotobuf

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


@dataclass
class nMkLpQ:
    mD: str
    oS: str
    gP: str
    iP: str
    dV: str
    uA: str


class qZxWvY:
    aB1 = "https://loginbp.ppmainecoonghj.com/MajorLogin"
    aB2 = "https://client.ind.freefiremobile.com/GetLoginData"

    kY1 = bytes([89, 103, 38, 116, 99, 37, 68, 69, 117, 104, 54, 37, 90, 99, 94, 56])
    kV1 = bytes([54, 111, 121, 90, 68, 114, 50, 50, 69, 51, 121, 99, 104, 106, 77, 37])

    rV1 = "OB55"
    gV1 = "1.132.9"

    uAp1 = [
        "GarenaMSDK/4.0.44(25028RN03A ;Android 15;ar;EG;app 1.132.1 2019121229;)",
        "GarenaMSDK/4.0.43(25028RN03A ;Android 14;en;IN;app 1.131.1 2019121229;)",
        "GarenaMSDK/4.0.45(25028RN03A ;Android 13;hi;IN;app 1.133.1 2019121229;)",
        "GarenaMSDK/4.0.42(25028RN03A ;Android 12;en;IN;app 1.130.1 2019121229;)",
        "GarenaMSDK/4.0.41(25028RN03A ;Android 11;hi;IN;app 1.129.1 2019121229;)",
        "GarenaMSDK/4.0.40(25028RN03A ;Android 10;en;IN;app 1.128.1 2019121229;)",
    ]

    iPp1 = [
        "49.36.180.10","49.36.180.22","49.36.181.15","49.36.181.30",
        "103.87.24.10","103.87.24.25","103.87.25.14","103.87.25.30",
        "115.99.10.20","115.99.10.35","115.99.11.40","115.99.11.55",
        "49.36.83.10","49.36.83.22","49.36.84.15","49.36.84.30",
        "103.25.12.10","103.25.12.25","103.25.13.14","103.25.13.30",
        "115.99.20.10","115.99.20.22","115.99.21.15","115.99.21.30",
        "49.36.100.10","49.36.100.22","49.36.101.15","49.36.101.30",
        "103.41.20.10","103.41.20.20","103.41.21.10","103.41.21.20",
        "115.99.30.10","115.99.30.22","115.99.31.15","115.99.31.30",
        "49.36.150.10","49.36.150.22","49.36.151.15","49.36.151.30",
    ]

    dPv1 = [
        ("Asus ASUS_AI2501_B","Android OS 12 / API-31 (SP1A.210812.016.C2)","Adreno (TM) 640"),
        ("Redmi Note 12 Pro","Android OS 13 / API-33 (TP1A.220624.014)","Adreno (TM) 618"),
        ("Samsung SM-M135F","Android OS 13 / API-33 (TP1A.220624.014)","Mali-G68"),
        ("Realme RMX3630","Android OS 12 / API-31 (SP1A.210812.016)","Adreno (TM) 610"),
        ("Vivo V2149","Android OS 13 / API-33 (TP1A.220624.014)","Adreno (TM) 642L"),
        ("OnePlus CPH2411","Android OS 13 / API-33 (TP1A.220624.014)","Adreno (TM) 730"),
        ("Poco M4 Pro 5G","Android OS 12 / API-31 (SP1A.210812.016)","Mali-G57 MC2"),
        ("iQOO I2012","Android OS 13 / API-33 (TP1A.220624.014)","Adreno (TM) 650"),
        ("Oppo CPH2477","Android OS 13 / API-33 (TP1A.220624.014)","Adreno (TM) 619"),
        ("Tecno KI8","Android OS 13 / API-33 (TP1A.220624.014)","Mali-G57"),
        ("Infinix X6819","Android OS 12 / API-31 (SP1A.210812.016)","Mali-G52 MC2"),
        ("Motorola moto g73","Android OS 13 / API-33 (TP1A.220624.014)","Adreno (TM) 619"),
        ("Xiaomi 2201122G","Android OS 13 / API-33 (TP1A.220624.014)","Adreno (TM) 730"),
        ("Realme RMX3700","Android OS 14 / API-34 (UP1A.231005.007)","Mali-G710"),
        ("OnePlus CPH2451","Android OS 13 / API-33 (TP1A.220624.014)","Adreno (TM) 740"),
        ("OPPO CPH2611","Android OS 14 / API-34 (UP1A.231005.007)","Adreno (TM) 720"),
        ("Samsung SM-G998B","Android OS 12 / API-31 (SP1A.210812.016)","Adreno (TM) 660"),
        ("Poco M2102J20SG","Android OS 13 / API-33 (TP1A.220624.014)","Adreno (TM) 660"),
        ("Vivo V2203","Android OS 12 / API-31 (SP1A.210812.016)","Mali-G710"),
        ("Xiaomi 2201117TG","Android OS 12 / API-31 (SP1A.210812.016)","Adreno (TM) 618"),
    ]

    def __init__(self, pRx: Optional[List[str]] = None, rOt: int = 20) -> None:
        self.pRx = pRx or []
        self.rOt = rOt
        self.cNt = 0
        self.sEs = self._bS()

    def _bS(self) -> requests.Session:
        sEs = requests.Session()
        aDp = requests.adapters.HTTPAdapter(pool_connections=20, pool_maxsize=20, max_retries=0)
        sEs.mount("https://", aDp)
        sEs.mount("http://", aDp)
        if self.pRx:
            pXy = random.choice(self.pRx)
            if not pXy.startswith("http"):
                pXy = f"http://{pXy}"
            sEs.proxies = {"http": pXy, "https": pXy}
        return sEs

    def _rS(self) -> None:
        self.cNt += 1
        if self.cNt >= self.rOt:
            self.cNt = 0
            self.sEs = self._bS()

    @classmethod
    def mKId(cls) -> nMkLpQ:
        mD, oS, gP = random.choice(cls.dPv1)
        return nMkLpQ(
            mD=mD, oS=oS, gP=gP,
            iP=random.choice(cls.iPp1),
            dV=f"Google|{uuid.uuid4()}",
            uA=random.choice(cls.uAp1),
        )

    @staticmethod
    def _eV(n: int) -> bytes:
        if n < 0:
            return b""
        bUf = bytearray()
        while True:
            bYt = n & 0x7F
            n >>= 7
            if n:
                bYt |= 0x80
            bUf.append(bYt)
            if not n:
                break
        return bytes(bUf)

    @classmethod
    def _eF(cls, fN: int, fV: Any) -> bytes:
        if isinstance(fV, int):
            return cls._eV((fN << 3) | 0) + cls._eV(fV)
        if isinstance(fV, (str, bytes)):
            rW = fV.encode() if isinstance(fV, str) else fV
            return cls._eV((fN << 3) | 2) + cls._eV(len(rW)) + rW
        return b""

    @classmethod
    def _sM(cls, fD: Dict[int, Any]) -> bytes:
        return b"".join(cls._eF(k, v) for k, v in fD.items())

    @classmethod
    def _eP(cls, rW: bytes) -> bytes:
        return AES.new(cls.kY1, AES.MODE_CBC, cls.kV1).encrypt(pad(rW, AES.block_size))

    _jR = re.compile(rb"eyJ[A-Za-z0-9_\-]+\.[A-Za-z0-9_\-]+\.[A-Za-z0-9_\-]+")

    @classmethod
    def _jX(cls, bDy: bytes) -> Optional[str]:
        if not bDy:
            return None
        for oFf in (0, 64, 4, 8, 16):
            try:
                dEc, _ = blackboxprotobuf.decode_message(bDy[oFf:] if oFf < len(bDy) else bDy)
                if not isinstance(dEc, dict):
                    continue
                for kEy in ('8', 8, b'8', 'jwt', b'jwt', 'token', b'token'):
                    if kEy not in dEc:
                        continue
                    vAl = dEc[kEy]
                    if isinstance(vAl, bytes) and vAl.startswith(b"eyJ"):
                        return vAl.decode("utf-8", "ignore")
                    if isinstance(vAl, str) and vAl.startswith("eyJ"):
                        return vAl
            except Exception:
                continue
        mTc = cls._jR.search(bDy)
        return mTc.group(0).decode("utf-8", "ignore") if mTc else None

    def mAjL(self, tKn: str, oId: str, iDv: nMkLpQ,
             lNg: str = "en") -> Optional[Dict[str, str]]:
        tSt = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
        fLd = {
            3: tSt, 4: "free fire", 5: 4,
            7: "1.132.9", 8: "2019116753",
            9: iDv.oS, 10: "Handheld", 11: iDv.mD,
            12: 1280, 13: 720, 14: "240",
            15: "x86-64 SSE3 SSE4.1 SSE4.2 AVX AVX2 | 2400 | 4",
            16: random.choice([5951, 6000, 6100, 5500, 6500]),
            17: iDv.gP, 18: "OpenGL ES 3.1 v1.46",
            19: iDv.dV, 20: iDv.iP,
            21: lNg, 22: oId, 23: "4", 24: "Handheld",
            25: iDv.mD, 26: "IND", 29: tKn, 30: 1,
            41: "Jio", 42: "WIFI",
            92: random.choice([19788, 20000, 21000]),
            93: "android_max", 97: 1, 98: 1,
            99: "4", 100: "4", 104: 77149, 105: 1,
        }
        pLd = self._eP(self._sM(fLd))
        hDr = {
            "User-Agent": iDv.uA,
            "Accept-Encoding": "deflate, gzip",
            "X-GA-SV": "1789535859",
            "Authorization": f"Bearer {tKn}",
            "X-GA": "v1 1",
            "ReleaseVersion": self.rV1,
            "Content-Type": "application/octet-stream",
            "X-Unity-Version": "2018.4.12f1",
            "Host": "loginbp.ppmainecoonghj.com",
        }
        try:
            rSp = self.sEs.post(self.aB1, headers=hDr, data=pLd, verify=False, timeout=8)
        except requests.RequestException:
            return None
        finally:
            self._rS()

        if rSp.status_code != 200 or len(rSp.content) < 20:
            return None
        jWt = self._jX(rSp.content)
        aId = self._aX(jWt, rSp.content)
        return {"account_id": str(aId), "jwt": jWt or ""} if aId else None

    @classmethod
    def _aX(cls, jWt: Optional[str], bDy: bytes) -> Optional[str]:
        if jWt and jWt.count(".") == 2:
            try:
                sEg = jWt.split(".")[1]
                sEg += "=" * (4 - len(sEg) % 4)
                dEc = json.loads(base64.urlsafe_b64decode(sEg))
                vAl = dEc.get("account_id") or dEc.get("external_id") or dEc.get("uid")
                if vAl:
                    return str(vAl)
            except Exception:
                pass
        for oFf in (0, 4, 8, 16, 64):
            try:
                dEc, _ = blackboxprotobuf.decode_message(bDy[oFf:] if oFf < len(bDy) else bDy)
                if not isinstance(dEc, dict):
                    continue
                for kEy in ('3', 3, b'3', 'account_id', b'account_id'):
                    if kEy in dEc:
                        vAl = dEc[kEy]
                        return vAl.decode("utf-8", "ignore") if isinstance(vAl, bytes) else str(vAl)
            except Exception:
                continue
        return None

    def gEtL(self, tKn: str, oId: str, iDv: nMkLpQ,
             lNg: str = "en") -> Dict[str, Any]:
        if not tKn or not oId:
            return {"ok": False, "c": 0xE01, "m": "arg"}
        tSt = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
        fLd = {
            3: tSt, 4: "free fire", 5: 1,
            7: self.gV1, 8: iDv.oS, 9: "Handheld",
            10: "Jio", 11: "WIFI",
            12: 1600, 13: 720, 14: "320",
            15: "ARM64 FP ASIMD AES | 2301 | 8", 16: 2799,
            17: iDv.gP, 18: "OpenGL ES 3.2 build 1.1@5425693",
            19: iDv.dV, 20: iDv.iP,
            21: lNg, 22: oId, 23: "4", 24: "Handheld",
            25: iDv.mD, 26: "IND", 29: tKn, 30: 1,
            41: "Jio", 42: "WIFI",
            57: "1ac4b80ecf0478a44203bf8fac6120f5",
            60: 19799, 61: 1198, 62: 5056, 64: 1430,
            65: 19999, 66: 1198, 67: 19799, 70: 4, 73: 2,
            74: "/data/app/com.dts.freefireth-FFifmAAfKh0HbXBegWOzaxw==/lib/arm64",
            76: 1,
            77: "4c322aeb56444feaa151d1ea91a8f7f2|/data/app/com.dts.freefireth-FFifmAAfKh0HbXBegWOzaxw==/base.apk",
            78: 6, 79: 2, 81: "64", 83: "2019120816",
            86: "OpenGLES2", 87: 3071, 88: 8,
            90: "Mumbai", 91: "DL", 92: 13080,
            93: "3rd_party", 95: 111207,
            96: '{"cur_rate":null,"support_etc2":false}',
            97: 1, 99: "30", 100: "38", 102: "47504412000e085134",
        }
        pLd = self._eP(self._sM(fLd))
        hDr = {
            "Host": "client.ind.freefiremobile.com",
            "User-Agent": "UnityPlayer/2022.3.47f1 (UnityWebRequest/1.0, libcurl/8.5.0-DEV)",
            "Accept": "*/*",
            "Accept-Encoding": "deflate, gzip",
            "Authorization": f"Bearer {tKn}",
            "X-GA": "v1 1",
            "ReleaseVersion": self.rV1,
            "Content-Type": "application/octet-stream",
            "X-Unity-Version": "2022.3.47f1",
        }
        try:
            rSp = self.sEs.post(self.aB2, headers=hDr, data=pLd, verify=False, timeout=8)
        except Exception:
            return {"ok": False, "c": 0xE02, "m": "net"}
        finally:
            self._rS()

        if rSp.status_code == 200:
            oNl = "OK"
            try:
                dEc, _ = blackboxprotobuf.decode_message(rSp.content)
                if isinstance(dEc, dict):
                    oNl = dEc.get("14", "OK")
                    if isinstance(oNl, bytes):
                        oNl = oNl.decode("utf-8", "ignore")
            except Exception:
                pass
            return {"ok": True, "c": 0x00, "m": str(oNl)}
        if rSp.status_code in (401, 403):
            return {"ok": False, "c": 0xE03, "m": "tok"}
        return {"ok": False, "c": 0xE00 + rSp.status_code, "m": "http"}
using Photon.Pun;
using Photon.Voice.Unity;
using UnityEngine;

public class VoiceManager : MonoBehaviourPun
{
    public Recorder recorder;

    private void Start()
    {
        if (photonView.IsMine)
        {
            recorder.TransmitEnabled = true;
        }
    }
}


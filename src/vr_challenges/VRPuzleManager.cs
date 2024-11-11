using UnityEngine;

public class VRPuzzleManager : MonoBehaviour
{
    public GameObject[] clues;
    private int cluesFound = 0;

    public void FindClue()
    {
        cluesFound++;
        CheckCompletion();
    }

    void CheckCompletion()
    {
        if (cluesFound == clues.Length)
        {
            Debug.Log("Puzzle solved!");
            // Trigger escape room exit or reward
        }
    }
}


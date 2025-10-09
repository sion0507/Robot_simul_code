import pybullet as p, pybullet_data
import math, os

# 기본 상수 (원하면 config에서 로드)
DT = 1/240.0
URDF_PATH = "/content/drive/MyDrive/Colab Notebooks/Robot_Simulation/urdf/diff_drive_min.urdf"

def connect(gui=False):
    """헤드리스 연결 + 평면 + 로봇 로드 + 좌/우 바퀴 조인트 인덱스 반환"""
    if p.isConnected():
        p.disconnect()
    cid = p.connect(p.GUI if gui else p.DIRECT)
    assert cid >= 0, "PyBullet connect failed"

    # 중력 및 타임스텝 설정 (여기로 옮김)
    p.setGravity(0,0,-9.81)
    p.setTimeStep(DT)

    
    robot = p.loadURDF(URDF_PATH, [0,0,0.05])

    # 로봇 불러온 후에 PyBullet 내장 데이터 경로 설정 (이 줄을 옮김)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    plane = p.loadURDF("plane.urdf")

    # 조인트 인덱스 찾기 및 마찰 설정
    n = p.getNumJoints(robot)
    jl = jr = None
    for j in range(n):
        name = p.getJointInfo(robot, j)[1].decode()
        if "left" in name:  jl = j
        if "right" in name: jr = j
        p.changeDynamics(robot, j, lateralFriction=1.5, rollingFriction=0.0, spinningFriction=0.15)
    assert jl is not None and jr is not None, "wheel joints not found"
    return robot, jl, jr

def base_pose(robot):
  """기체의 (x,y,z)와 yaw(라디안) 반환"""
  pos, orn = p.getBasePositionAndOrientation(robot)
  yaw = p.getEulerFromQuaternion(orn)[2] # roll(x축 중심 회전), pitch(y축 중심), yaw(z축 중심) 중 yaw 만 선탣ㄱ
  return pos, yaw

def step_n(n):
  """시뮬레이션 n스텝 실행"""
  for _ in range(int(n)):
    p.stepSimulation()
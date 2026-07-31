import math

class EuclideanTracker:
    """Assigns persistent tracking IDs to detected objects across video frames."""
    def __init__(self, max_disappeared=15):
        self.next_object_id = 101
        self.objects = {}       # id -> centroid (x, y)
        self.disappeared = {}   # id -> frame_count

    def update(self, rects):
        """
        rects: list of [x, y, w, h, label, confidence]
        Returns: list of dicts with assigned 'id'
        """
        if len(rects) == 0:
            for obj_id in list(self.disappeared.keys()):
                self.disappeared[obj_id] += 1
                if self.disappeared[obj_id] > 15:
                    del self.objects[obj_id]
                    del self.disappeared[obj_id]
            return []

        input_centroids = []
        for r in rects:
            cx = int(r[0] + r[2] / 2.0)
            cy = int(r[1] + r[3] / 2.0)
            input_centroids.append((cx, cy))

        # If currently tracking no objects, register all
        if len(self.objects) == 0:
            tracked_results = []
            for i, r in enumerate(rects):
                obj_id = self.next_object_id
                self.next_object_id += 1
                self.objects[obj_id] = input_centroids[i]
                self.disappeared[obj_id] = 0
                
                tracked_results.append({
                    "id": f"ID #{obj_id}",
                    "x": r[0], "y": r[1], "width": r[2], "height": r[3],
                    "label": r[4], "confidence": r[5]
                })
            return tracked_results

        # Match existing centroids to input centroids
        object_ids = list(self.objects.keys())
        object_centroids = list(self.objects.values())

        distances = []
        for oc in object_centroids:
            row = []
            for ic in input_centroids:
                dist = math.hypot(oc[0] - ic[0], oc[1] - ic[1])
                row.append(dist)
            distances.append(row)

        used_rows = set()
        used_cols = set()

        tracked_results = []

        # Find closest matches
        for _ in range(min(len(object_ids), len(input_centroids))):
            min_dist = float('inf')
            min_row, min_col = -1, -1

            for r_idx in range(len(object_ids)):
                if r_idx in used_rows: continue
                for c_idx in range(len(input_centroids)):
                    if c_idx in used_cols: continue
                    if distances[r_idx][c_idx] < min_dist:
                        min_dist = distances[r_idx][c_idx]
                        min_row, min_col = r_idx, c_idx

            if min_dist > 150: # Threshold max jump
                break

            used_rows.add(min_row)
            used_cols.add(min_col)

            obj_id = object_ids[min_row]
            self.objects[obj_id] = input_centroids[min_col]
            self.disappeared[obj_id] = 0

            r = rects[min_col]
            tracked_results.append({
                "id": f"ID #{obj_id}",
                "x": r[0], "y": r[1], "width": r[2], "height": r[3],
                "label": r[4], "confidence": r[5]
            })

        # Register unallocated new input centroids
        for c_idx in range(len(input_centroids)):
            if c_idx not in used_cols:
                obj_id = self.next_object_id
                self.next_object_id += 1
                self.objects[obj_id] = input_centroids[c_idx]
                self.disappeared[obj_id] = 0
                
                r = rects[c_idx]
                tracked_results.append({
                    "id": f"ID #{obj_id}",
                    "x": r[0], "y": r[1], "width": r[2], "height": r[3],
                    "label": r[4], "confidence": r[5]
                })

        return tracked_results
